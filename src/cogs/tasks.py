import datetime
from discord.ext import commands, tasks
from services.news_search import search_news
from services.app_validador import enviar_para_ia_validar
from database.database import buscar_noticias, buscar_servidores, inserir_noticias, inserir_canal_servidor
from utils.embeds import criar_embed_noticia

fuso_br = datetime.timezone(datetime.timedelta(hours=-3)) #Fuso-horario do Brasil

#Task de buscar noticia "Acorda" a cada 6 horas 
times = [
    datetime.time(hour=8, tzinfo=fuso_br),
    datetime.time(hour=14, tzinfo=fuso_br),
    datetime.time(hour=20, tzinfo=fuso_br),
    datetime.time(hour=2, tzinfo=fuso_br)
]

class TasksBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.search_task.start()

    def cog_unload(self):
        self.search_task.cancel()

    @tasks.loop(time=times)
    async def search_task(self):
        print("Tarefa Rodando!")
        urls_list, dados_banco = await search_news()
        for noticia in dados_banco:
            if buscar_noticias(noticia['id_noticia']): #Busca as noticias no banco para ver se existem, se sim, pula
                continue
            
            # Envia para a IA
            resultado_ia = await enviar_para_ia_validar(noticia['url'])
            
            #Manda o resultado enviado pela IA para as embeds e encaminha
            if resultado_ia and resultado_ia.get("relevante") is True:
                embed,view = criar_embed_noticia(resultado_ia)
                
                canais = buscar_servidores()
            
                for id_canal in canais:
                    canal = self.bot.get_channel(id_canal)
                    if canal:
                        await canal.send(embed=embed, view=view)
                
                #Insere a noticia encaminhada no banco para evitar duplicacao posterior
                inserir_noticias(
                    noticia['id_noticia'], 
                    noticia['titulo'], 
                    noticia['autor'], 
                    noticia['url'], 
                    noticia['postado_em'], 
                    noticia['tag']
                )
        
async def setup(bot):
    await bot.add_cog(TasksBot(bot))
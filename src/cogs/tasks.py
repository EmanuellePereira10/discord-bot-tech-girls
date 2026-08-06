import datetime
from discord.ext import commands, tasks
from services.news_search import search_news
from services.app_validador import enviar_para_ia_validar
from database.database import buscar_noticias, buscar_servidores, inserir_noticia
import asyncio
from utils.embeds import criar_embed_noticia

fuso_br = datetime.timezone(datetime.timedelta(hours=-3)) #Fuso-horario do Brasil

class TasksBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.search_task.start() #Apagada devido a ser inicializada apenas pelo /setupnews

    def cog_unload(self):
        self.main_task.cancel()

    #@tasks.loop(minutes=10)
    @tasks.loop(seconds=10)
    async def main_task(self):
        print("\n\nTarefa de automatização Rodando!")
        
        canais = buscar_servidores()
        if canais == []:
            print("\nNenhum canal registrado no banco, cancelando execução das tasks")
            return
        
        urls_list, dados_banco = await search_news()
        for noticia in reversed(dados_banco):
            if buscar_noticias(noticia['id_noticia']): #Busca as noticias no banco para ver se existem, se sim, pula
                continue
            
            # Envia para a IA
            resultado_ia = await enviar_para_ia_validar(noticia['url'])
            
            await asyncio.sleep(2) #Pausa pra nao estourar o limite da API do Gemini
            
            #Manda o resultado enviado pela IA para uma fila de noticias
            if resultado_ia and resultado_ia.get("relevante") is True:
                embed, view = criar_embed_noticia(resultado_ia)
                
                for id_canal in canais:
                    canal = self.bot.get_channel(id_canal)
                    if canal:
                        await canal.send(embed=embed, view=view)
          
                #Insere a noticia encaminhada no banco para evitar duplicacao       posterior
                inserir_noticia(
                    noticia['id_noticia'], 
                    noticia['titulo'], 
                    noticia['autor'], 
                    noticia['url'], 
                    noticia['postado_em'], 
                    noticia['tag']
                )
                print(f"\nNotícia enviada e salva: {noticia['titulo']}")
                
    @main_task.error
    async def main_task_error(self, error):
        print(f"\nERRO NA TASK: {error}")
        
        
async def setup(bot):
    await bot.add_cog(TasksBot(bot))
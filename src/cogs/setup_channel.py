import discord
from discord import app_commands
from discord.ext import commands
#from database.database import inserir_canal_servidor


#Aguardando funcoes do database.py para enviar o id do servidor e o id do canal para o banco de dados

class SetupChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="setupnews", description="Configura o canal onde as noticias serao encaminhadas")
    @app_commands.checks.has_permissions(administrator=True)
    async def channel(self, interaction: discord.Interaction):
        #inserir_canal_servidor(id_guild=interaction.guild.id, id_channel=interaction.channel.id)
        
        await interaction.response.send_message(f'Canal para noticias configurado com sucesso!')
        print(interaction.channel.id, interaction.guild.id)     
        
        task_cog = self.bot.get_cog("TasksTeste") #Utilizar classe de TasksBot apos conclusao
        
        if task_cog:
            if not task_cog.search_task_teste.is_running(): #Remover _teste apos conclusao
                task_cog.search_task_teste.start()

    @channel.error
    async def channel_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.errors.MissingPermissions):
            await interaction.response.send_message(f'Apenas administradores podem utilizar esse comando!', ephemeral=True)                    
          

async def setup(bot):

    await bot.add_cog(SetupChannel(bot))
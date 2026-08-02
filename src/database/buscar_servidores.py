import sqlite3

def buscar_servidores():
    conexao = sqlite3.connect("bot.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM canais_configurados")
    resultado = cursor.fetchall()
    
    if resultado != []:
        return ("canais encontrados", resultado)
    else:
        return ("canais nao encontrados")

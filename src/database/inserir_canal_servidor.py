import sqlite3

def inserir_canal_servidor(id_guild, id_channel, criado_em):
    conexao = sqlite3.connect("bot.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO canais_configurados(id_guild, id_channel, criado_em) VALUES (?, ?, ?)", (id_guild, id_channel, criado_em))
    conexao.commit()
    id_gerado = cursor.lastrowid
    return ("canal inserido", id_gerado)

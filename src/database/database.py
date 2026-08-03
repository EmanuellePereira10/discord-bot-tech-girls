import sqlite3

#Insere as noticias "publicadas" no discord no banco de dados para evitar noticias duplicadas
def inserir_noticia(id_noticia, titulo, autor, url, postado_em, tag):
    conexao = sqlite3.connect("bot.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("INSERT INTO noticias_postadas (id_noticia, titulo, autor, url, postado_em, tag) VALUES (?, ?, ?, ?, ?, ?)", (id_noticia, titulo, autor, url, postado_em, tag))
        conexao.commit()
        return ("noticia aceita", id_noticia)
    except:
        cursor.execute("SELECT id_noticia FROM noticias_postadas WHERE url = ?", (url,))
        resultado = cursor.fetchone()
        return ("noticia recusada", resultado[0])
    
#Busca as noticias no banco de dados
def buscar_noticias(id_noticia):
    conexao = sqlite3.connect("bot.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id_noticia, titulo, autor, url, postado_em, tag FROM noticias_postadas WHERE id_noticia = ?", (id_noticia,))
    resultado = cursor.fetchone()
    
    if resultado is not None:
        return ("noticia encontrada", resultado)
    else:
        return ("noticia nao encontrada")
    
#Busca os canais configurados para o envio das noticias
def buscar_servidores():
    conexao = sqlite3.connect("bot.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM canais_configurados")
    resultado = cursor.fetchall()
    
    if resultado != []:
        return ("canais encontrados", resultado)
    else:
        return ("canais nao encontrados")
    
#Insere o id do canal e do servidor onde serao encaminhadas no banco de dados
def inserir_canal_servidor(id_guild, id_channel, criado_em):
    conexao = sqlite3.connect("bot.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO canais_configurados(id_guild, id_channel, criado_em) VALUES (?, ?, ?)", (id_guild, id_channel, criado_em))
    conexao.commit()
    id_gerado = cursor.lastrowid
    return ("canal inserido", id_gerado)

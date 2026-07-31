import sqlite3

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

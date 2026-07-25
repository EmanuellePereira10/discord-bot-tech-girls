import sqlite3
def inserir_noticia(titulo, autor, url, postado_em, tag):
    conexao = sqlite3.connect("bot.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("INSERT INTO noticias_postadas (titulo, autor, url, postado_em, tag) VALUES (?, ?, ?, ?, ?)", (titulo, autor, url, postado_em, tag))
        conexao.commit()
        id_gerado = cursor.lastrowid
        return ("noticia aceita", id_gerado)
    except:
        cursor.execute("SELECT id_noticia FROM noticias_postadas WHERE url = ?", (url,))
        resultado = cursor.fetchone()
        return ("noticia recusada", resultado[0])

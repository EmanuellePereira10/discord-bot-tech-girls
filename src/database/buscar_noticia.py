import sqlite3

def buscar_noticia(id_noticia):
    conexao = sqlite3.connect("bot.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id_noticia, titulo, autor, url, postado_em, tag FROM noticias_postadas WHERE id_noticia = ?", (id_noticia,))
    resultado = cursor.fetchone()
    
    if resultado is not None:
        return ("noticia encontrada", resultado)
    else:
        return ("noticia nao encontrada")

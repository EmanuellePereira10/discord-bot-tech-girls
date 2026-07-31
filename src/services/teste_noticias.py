import asyncio
from pprint import pprint
from news_search import search_news

async def testar():
    urls, noticias = await search_news()
    
    print("============TESTANDO URLS=============")
    pprint(urls)
    
    print("\n============TESTANDO DICIONARIOS=============")
    pprint(noticias if noticias else "Lista vazia")

asyncio.run(testar()) 
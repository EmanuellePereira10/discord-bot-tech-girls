# 🤖📰 Tech News Bot

## Sobre o projeto

Bot desenvolvido para buscar automaticamente as notícias mais recentes de tecnologia no *TabNews* e publicá-las em um canal do Discord da comunidade *Tech Girls*.

O projeto utiliza um *agente de IA* para ler o conteúdo completo de cada notícia, identificar se ela é relevante para a comunidade, gerar um resumo em linguagem simples e organizar as informações antes da publicação.

> ⚠️ *Projeto em desenvolvimento.* Algumas funcionalidades ainda estão sendo implementadas.

---

## Como funciona

1. O bot busca novas notícias na API do TabNews.
2. O agente de IA analisa o conteúdo completo de cada notícia.
3. A IA gera um JSON com título, resumo, tags e link.
4. O embeds.py transforma essas informações em um Embed do Discord.
5. O bot publica a notícia no canal configurado.
6. Futuramente, um banco de dados evitará publicações duplicadas.

---

## Estrutura do projeto

- *bot.py* — inicia o bot e realiza a conexão com o Discord.
- *news_search.py* — busca as notícias na API do TabNews.
- *tasks.py* — executa automaticamente a busca de notícias a cada 6 horas.
- *embeds.py* — cria os Embeds que serão enviados ao Discord.
- *setup_channel.py* — configura o canal onde as notícias serão publicadas.
- *testar_embeds.py* — arquivo utilizado durante o desenvolvimento para testar os Embeds.

---

## Tecnologias

- Python
- discord.py
- aiohttp
- API pública do TabNews

---

## Próximos passos

- Integrar o agente de IA ao fluxo automático.
- Implementar um banco de dados para evitar notícias repetidas.
- Finalizar e otimizar o fluxo de publicação.

---

## Equipe

Projeto desenvolvido em equipe como parte do *Tech Girls Challenge #1* 

- Thais
- Maria Fernanda
- Andressa 
- Lucila

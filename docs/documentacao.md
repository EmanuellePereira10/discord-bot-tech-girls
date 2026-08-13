# 🤖📰 Tech News Bot

## Sobre o projeto

Bot desenvolvido para buscar automaticamente notícias recentes de tecnologia no TabNews e publicá-las em um canal do Discord da comunidade Tech Girls.

O projeto utiliza um agente de IA com Gemini 3.5 Flash para acessar o conteúdo completo das notícias, analisar sua relevância, gerar um resumo em linguagem simples e organizar as informações antes da publicação.

O fluxo foi desenvolvido para funcionar de forma automática, desde a busca da notícia até seu armazenamento no banco de dados, evitando publicações duplicadas.

---

## Como funciona

#### 1. Configuração do canal 
O bot é iniciado através da função `setup_channel`, que configura o canal do Discord onde as notícias serão publicadas.

#### 2. Busca das notícias 
A função `news_search` consulta a **API do TabNews** e retorna as notícias encontradas com seus respectivos IDs e URLs.

#### 3. Verificação de duplicidade
Antes de enviar uma notícia para o agente de IA, o sistema verifica no banco de dados se aquela notícia ou URL já foi registrada, evitando publicações duplicadas.

#### 4. Análise com Inteligência Artificial
As notícias novas são enviadas ao agente de IA, que acessa a URL, lê o conteúdo e retorna uma estrutura em **JSON** contendo:

- Título
- Resumo
- Tags
- URL

#### 5. Normalização dos dados 
Os dados retornados pelo agente passam por funções de **normalização**, garantindo que as informações estejam no formato esperado.

#### 6. Processamento da tarefa 
A função de tarefas recebe os dados estruturados e envia as informações para `embeds.py`.

#### 7. Criação do Embed
O `embeds.py` transforma os dados em **Embeds do Discord**.

#### 8. Publicação no Discord 
O bot publica automaticamente a notícia no canal configurado.

#### 9. Armazenamento  
Após a publicação, os dados da notícia são armazenados no **banco de dados**, permitindo que sejam utilizados nas próximas verificações.

----
## 🔄 Automação

O fluxo de busca e publicação é executado automaticamente em um intervalo de 4 horas, mantendo o canal atualizado com novas notícias de tecnologia.

----
## 🧠 Uso de Inteligência Artificial

O agente de IA é responsável por analisar o conteúdo das notícias antes da publicação.

Ele:

Acessa a notícia através da URL recebida;
Lê o conteúdo da página;
Analisa a relevância da notícia;
Gera um resumo;
Identifica tags;
Organiza as informações em formato JSON.

Isso permite que o bot não apenas copie notícias, mas processe e organize o conteúdo antes de apresentá-lo à comunidade.

---- 
## 🗄️ Banco de dados

Após a publicação, as informações processadas são armazenadas no banco de dados.

O armazenamento também é utilizado para verificar se uma notícia ou URL já foi publicada anteriormente.

Dessa forma, antes de iniciar um novo ciclo de processamento, o sistema consulta o banco para evitar notícias duplicadas.

---

## 📸 Prints do projeto

#### Aplicação funcionando:

falta o print 

#### Embeds publicados no Discord:

falta o print 

#### Comando /setupchannel:

falta o print 

---

## Estrutura do projeto

- bot.py — inicia o bot e realiza a conexão com o Discord.
- news_search.py — consulta a API do TabNews e realiza a busca das notícias.
- tarefas.py — controla a execução automática do processo de busca e publicação.
- embeds.py — transforma os dados estruturados em Embeds do Discord.
- setup_channel.py — configura o canal do Discord onde as notícias serão publicadas.
- testar_embeds.py — utilizado durante o desenvolvimento para testes dos Embeds.

---

## Tecnologias

- Python
- discord.py
- aiohttp
- API pública do TabNews
- Gemini 3.5 Flash
-Banco de dados
-Discord

---

## ✅ Status

Projeto finalizado.

O bot possui fluxo automatizado de busca, análise por IA, normalização, publicação no Discord e armazenamento das notícias no banco de dados, incluindo uma verificação para evitar publicações duplicadas

----
## O que isso significa na prática

Com esse fluxo funcionando de ponta a ponta, a comunidade Tech Girls passa a receber notícias de tecnologia atualizadas automaticamente no Discord, sem que ninguém precise buscar ou publicar manualmente — e sem risco de a mesma notícia aparecer duas vezes no canal.

----

## 📖 Miniglossário

| Termo | O que significa |
|---|---|
| **API** | Uma "porta de entrada" que permite que o bot peça informações a outro sistema (nesse caso, o TabNews) de forma automática. |
| **JSON** | Um formato de texto organizado em campos, parecido com uma ficha preenchida — facilita que diferentes partes do sistema "conversem" entre si. |
| **Embed** | O cartão visual formatado que o Discord mostra, com título, resumo e link organizados — diferente de uma mensagem de texto simples. |
| **Agente de IA** | A parte do sistema que usa inteligência artificial (Gemini) para ler, entender e resumir o conteúdo da notícia antes de publicar. |
| **Normalização** | Processo de ajustar os dados recebidos para que fiquem sempre no mesmo formato, independente de pequenas variações na resposta da IA. |
| **Banco de dados** | Onde ficam guardadas as notícias já publicadas, usado para verificar duplicidade antes de postar uma nova. |

---

## Equipe

Projeto desenvolvido em equipe como parte do *Tech Girls* 

- Thais
- Maria Fernanda
- Andressa
- Lucila



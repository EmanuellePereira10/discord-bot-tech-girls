# Discord Bot - Tech Girls

## Objetivo

Desenvolver um bot para a comunidade Tech Girls, integrada ao Discord, que automatize o compartilhamento de notícias de tecnologia por meio da API do TabNews e divulgue vagas na área tech.

## Equipe

- Thais
- Maria
- Lucila
- Andressa
  
## Stack

- Python 3.14
- discord.py
- SQLite Studio
- API TabNews

## Banco de Dados

Tabela 1: noticias_postadas

Guarda o ID da notícia, evitando duplicidade.

Colunas
- id_noticia - id da notícia conforme no site TabNews
- titulo - título da notícia postada no TabNews
- url - url da notícia
- autor - identificação de quem postou a notícia no site
- tag - classificador de assunto da notícia
- postado_em - data em que a notícia foi postada no bot

Tabela 2: canais_configurados

Guarda em qual servidor/canal o bot deve postar

Colunas
- id_canal - id gerado internamente para o canal de notícias
- id_guild - id do servidor discord
- id_channel - identificador do discord
- criado_em - data de criação do servidor

## Como rodar com Docker

### Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado
- [Docker Compose](https://docs.docker.com/compose/install/) instalado (versão com plugin: `docker compose`)

### 1) Configurar variáveis de ambiente

Na raiz do projeto, crie seu arquivo `.env` a partir do exemplo:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e preencha **todas** as variáveis obrigatórias:

| Variável | Obrigatória para | Descrição |
|---|---|---|
| `GEMINI_API_KEY` | Validação de notícias | Chave da API do Google Gemini |
| `BOT_TOKEN` | Bot Discord completo | Token do bot gerado no Discord Developer Portal |
| `DEV_GUILD_ID` | Bot Discord completo | ID do servidor Discord para sincronização de comandos |

> **Atenção:** sem o `BOT_TOKEN` e o `DEV_GUILD_ID` o bot se conectará mas não conseguirá sincronizar nenhum comando no servidor Discord.

### 2) Build da imagem

```bash
docker compose build
```

### 3) Subir a aplicação

```bash
docker compose up
```

Para rodar em segundo plano:

```bash
docker compose up -d
```

### 4) Ver logs da execução

```bash
docker compose logs -f
```

### 5) Parar os containers

```bash
docker compose down
```

## Fluxo executado no container

O container executa o arquivo `src/bot.py`, que realiza em sequência:

1. Carrega as variáveis de ambiente do arquivo `.env`
2. Inicializa as tabelas do banco de dados SQLite (`bot.db`) caso ainda não existam
3. Conecta os "cogs" de tarefas (`tasks`) e configuração de canal (`setup_channel`)
4. Sincroniza os slash commands no servidor Discord configurado em `DEV_GUILD_ID`
5. Mantém o bot online e aguarda os horários programados (08h, 14h, 20h e 02h, horário de Brasília) para buscar e publicar notícias via TabNews + validação Gemini


## Dependências

Para rodar o bot e os serviços de busca de notícias, o projeto utiliza as seguintes bibliotecas Python:

* **`discord.py`**: Framework para interação com a API do Discord.
* **`aiohttp`**: Biblioteca assíncrona para requisições HTTP (instalada automaticamente junto com o `discord.py`), utilizada na integração com a API do TabNews.
* **`python-dotenv`**: Gerenciamento de variáveis de ambiente (chaves de API, ID do servidor de testes e tokens).

### Para instalar as dependências
No terminal, instale os pacotes necessários:

```bash
pip install discord.py python-dotenv

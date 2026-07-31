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

- Docker instalado
- Docker Compose instalado (ou plugin `docker compose`)

### 1) Configurar variáveis de ambiente

Na raiz do projeto, crie seu arquivo `.env` a partir do exemplo:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e preencha, no mínimo:

- `GEMINI_API_KEY`

Observação:
- `BOT_TOKEN` e `DEV_GUILD_ID` só são necessários quando for executar o bot completo no Discord.

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

## Fluxo executado no container hoje

O container está configurado para executar o arquivo `main_teste.py`, que faz:

1. Busca notícias na API do TabNews
2. Envia conteúdo para validação no Gemini
3. Exibe no terminal o JSON retornado pela validação

Os arquivos em `Validador_IA/dados_teste/` são apenas artefatos de teste e não fazem parte do fluxo final de produção.


## Dependências

Para rodar o bot e os serviços de busca de notícias, o projeto utiliza as seguintes bibliotecas Python:

* **`discord.py`**: Framework para interação com a API do Discord.
* **`aiohttp`**: Biblioteca assíncrona para requisições HTTP (instalada automaticamente junto com o `discord.py`), utilizada na integração com a API do TabNews.
* **`python-dotenv`**: Gerenciamento de variáveis de ambiente (chaves de API, ID do servidor de testes e tokens).

### Para instalar as dependências
No terminal, instale os pacotes necessários:

```bash
pip install discord.py python-dotenv

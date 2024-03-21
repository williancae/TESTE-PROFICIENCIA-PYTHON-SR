# TESTE PROFICIENCIA PYTHON SR

## Descrição

O teste consiste em criar uma API que faz a conversão moedas.

## Dependências

Para executar o projeto é necessário ter instalado:

- Docker
- Docker Compose

## Execução

Para executar o projeto, basta rodar o comando abaixo na raiz do projeto:

#### Modo de Desenvolvimento

```bash
docker-compose up dev
```

#### Modo de Produção

```bash
docker-compose up prod
```

## Swagger

Para acessar a documentação da API, acesse o link abaixo:
<br/><b>Obs.: Deve-se estar com o projeto rodando.</b>

- <http://localhost:8000/docs>

## Teste rapido de API

Rode o projeto em modo de desenvolvimento e execute o comando abaixo:

```bash
docker-compose up dev
```

Chame a API com o comando abaixo:

```bash
curl -X 'GET' \
  'http://localhost:8000/exchange-rate/?currency_from=BRL&currency_to=USD&amount=25' \
  -H 'accept: application/json'
```

<hr/>

## Resolução do Teste

### Sobre a API

Desenvolvi uma API utilizando a biblioteca FastAPI, uma ferramenta moderna, rápida e fácil de usar para a construção de APIs. Além disso, configurei containers Docker para executar a aplicação tanto em ambiente de desenvolvimento quanto em produção.

### Solução proposta

Fiz uma integração com uma API publica que fornece a cotação das moedas, a [AwesomeAPI - API de Cotações](https://docs.awesomeapi.com.br/api-de-moedas), para fazer a conversão das moedas e configurei um mecanismo de cacheamento para evitar chamadas desnecessárias a essa API e melhorar a performance da aplicação.

# Especificação — GET /health

Endpoint público e sem parâmetros usado para verificar o processo HTTP da API.

## Resposta saudável

- Status HTTP: `200 OK`
- Content-Type: `application/json`

```json
{"status": "healthy", "service": "atreides-agro-api"}
```

Este é um teste de vivacidade. A prontidão do ambiente também depende do
healthcheck próprio do PostgreSQL/PostGIS. Uma checagem de banco dentro da API
deve surgir quando rotas de negócio dependerem dele.

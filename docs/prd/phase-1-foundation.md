# PRD — Fase 1: Fundação

## Objetivo

Permitir que um desenvolvedor com Docker inicie uma API FastAPI e um
PostgreSQL/PostGIS saudáveis com um único comando.

## Escopo

- API com `GET /health`.
- PostgreSQL 16 com extensão PostGIS.
- Persistência e healthchecks gerenciados pelo Compose.
- Teste e lint executáveis no container da API.
- Configuração por ambiente e documentação inicial.

## Fora do escopo

Catálogo, autenticação, agente de IA, Redis, pgvector, frontend, mapas,
dashboards, pipelines e orquestração.

## Critérios de aceite

1. `docker compose up -d --build` conclui sem erro.
2. `docker compose ps` mostra `api` e `postgres` saudáveis.
3. `GET /health` responde HTTP 200 com o nome do serviço.
4. `docker compose exec api pytest` passa.
5. Nenhum segredo real está versionado.

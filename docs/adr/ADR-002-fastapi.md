# ADR-002 — FastAPI para a API

- Status: aceito
- Data: 2026-08-18

## Contexto

A plataforma precisa de uma API Python tipada, testável e extensível.

## Decisão

Usar FastAPI com Pydantic e separação pequena entre rotas, schemas e config.
SQLAlchemy e Alembic serão usados quando surgirem modelos reais.

## Alternativas consideradas

- Flask: exigiria mais decisões para validação e documentação.
- Django: oferece recursos não necessários nesta fundação.

## Consequências

Há OpenAPI automática e validação tipada. A estrutura cresce com os casos reais.

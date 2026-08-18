# ADR-003 — PostgreSQL com PostGIS

- Status: aceito
- Data: 2026-08-18

## Contexto

Entidades futuras exigirão consultas geoespaciais e integridade relacional.

## Decisão

Usar PostgreSQL 16 com PostGIS 3.5 e validar a extensão no healthcheck.

## Alternativas consideradas

- PostgreSQL sem PostGIS: não atende às consultas espaciais planejadas.
- Banco geográfico separado: adicionaria sincronização prematura.
- pgvector: adiado até existir um caso de recuperação vetorial.

## Consequências

Dados transacionais e geográficos compartilharão consistência e SQL.

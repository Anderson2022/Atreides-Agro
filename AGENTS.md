# AGENTS.md

## Princípios do projeto

- Todo componente executável deve funcionar via Docker Compose.
- Mantenha a arquitetura incremental; não adicione serviços sem necessidade.
- A IA decide o que dizer; o backend controla e valida o que pode ser feito.
- Nunca permita SQL arbitrário produzido por LLM nem ações irreversíveis sem
  regras de negócio e, quando aplicável, aprovação humana.
- Use apenas dados sintéticos para pessoas, clientes, fazendas e operações.
- Nunca versione segredos nem registre senhas, tokens ou chaves em logs.

## Fluxo de trabalho

1. Analise o estado e os impactos arquiteturais.
2. Implemente a menor entrega coerente.
3. Execute testes e lint dentro dos containers.
4. Valide build, inicialização e healthchecks do Docker Compose.
5. Atualize documentação e ADRs quando houver decisão relevante.

## Convenções atuais

- Backend: Python 3.12, FastAPI, Pydantic, pytest e Ruff.
- Banco: PostgreSQL 16 com PostGIS.
- Código em `backend/app` e testes em `backend/tests`.
- Migrações futuras usam Alembic; `database/init` apenas prepara extensões.
- Configurações são centralizadas em `backend/app/core/config.py`.
- Chamadas futuras a LLM devem ficar atrás de uma abstração de provedor.

## Escopo vigente

A Fase 1 inclui somente fundação, `/health`, PostGIS, Docker, testes e docs. Não
implemente catálogo, agente, mapas ou pipelines sem nova etapa aprovada.

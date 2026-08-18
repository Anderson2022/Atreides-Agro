# ADR-001 — Ambiente Docker-first

- Status: aceito
- Data: 2026-08-18

## Contexto

O projeto precisa ser reproduzível sem instalações locais de linguagem ou banco.

## Decisão

Docker Compose é a interface operacional. Imagens declaram dependências;
healthchecks controlam a inicialização; um volume persiste o PostgreSQL.

## Alternativas consideradas

- Instalação local: descartada por gerar divergência entre ambientes.
- Kubernetes: descartado por complexidade incompatível com esta fase.

## Consequências

Docker é o único requisito local. Builds levam tempo, mas são reproduzíveis.

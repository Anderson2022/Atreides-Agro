# Arquitetura da fundação

```text
Cliente / healthcheck
         |
         v
  FastAPI (api:8000)
         |
         v
PostgreSQL 16 + PostGIS (postgres:5432)
         |
         v
 volume postgres_data
```

O Compose supervisiona os serviços. A API só inicia após o banco passar por uma
consulta a `PostGIS_Version()`. `/health` confirma a vivacidade HTTP sem acoplar
prematuramente a rota ao banco.

Configurações chegam por ambiente e são centralizadas com Pydantic. SQLAlchemy
e Alembic estão disponíveis para a próxima fase, sem modelos vazios agora.

# Technology Stack & Constraints

## Stack & Version Matrix
- **Language:** Python 3.11+
- **Web Framework:** FastAPI (ASGI) with `uvicorn`
- **Database & ORM:** PostgreSQL (Neon.tech serverless), `SQLModel` (combining SQLAlchemy + Pydantic)
- **Migrations:** `Alembic`
- **Validation & Settings:** `Pydantic v2` and `pydantic-settings`
- **HTTP Client:** `httpx` (Asynchronous)
- **Machine Learning:** `scikit-learn`, `pandas`, `joblib`
- **Frontend Layer:** Jinja2 templates, HTMX (dynamic updates), Tailwind CSS, Chart.js
- **Auth & Security:** Google OAuth 2.0 (`authlib`/`fastapi-sso`) with single-email address whitelist
- **Infrastructure & Cloud:** Docker, AWS Lambda (`Mangum` adapter), API Gateway, AWS SSM Parameter Store, EventBridge Cron, Terraform (IaC)

## Code Quality & Architecture Rules
1. **Layered Architecture:** Enforce clean separation across directories:
   - `app/core/`: Configuration, database engine setup, global security.
   - `app/models/`: SQLModel entities and database schemas.
   - `app/api/`: FastAPI route handlers and request/response models.
   - `app/services/`: Core business logic (Lunch Flow client, ML engine, transfer detection).
   - `scripts/`: Offline utilities (CSV ingestion, model training).
2. **Type Safety:** All Python functions must include explicit type hints.
3. **Environment Isolation:** Never hardcode credentials. Use `pydantic-settings` to parse values from `.env`.
4. **Database Migrations:** Never alter SQLModel fields without generating an Alembic migration (`alembic revision --autogenerate`).
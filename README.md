# Serverless Personal Finance Tracker & ML Categorizer

An end-to-end, zero-cost personal finance application hosted on AWS. The system automatically normalizes transaction data from multi-bank CSV exports and live Open Banking REST APIs (Lunch Flow), processes them through a multi-tier categorization engine, and renders financial insights via a dynamic web dashboard.

---

## 🏛 Architecture Overview

- **Compute:** AWS Lambda (running containerized FastAPI via Mangum adapter)
- **API Management:** AWS API Gateway
- **Database:** Neon Serverless PostgreSQL
- **Scheduling:** AWS EventBridge (triggers daily bank sync)
- **Secrets:** AWS SSM Parameter Store
- **Infrastructure as Code:** Terraform
- **Frontend:** FastAPI + Jinja2 + HTMX + Tailwind CSS + Chart.js

---

## 🛠 Tech Stack

| Layer | Technologies |
| :--- | :--- |
| **Backend** | Python 3.11+, FastAPI, SQLModel, Alembic |
| **Database** | PostgreSQL (Neon.tech), Pydantic v2 |
| **Data & ML** | scikit-learn, pandas, httpx (Async HTTP) |
| **Frontend** | Jinja2, HTMX, Tailwind CSS, Chart.js |
| **DevOps** | Docker, Terraform, AWS Lambda, EventBridge |

---

## 🗺 Project Epics & Roadmap

1. **`epic: env`** — Environment Setup, Dependencies & Configuration
2. **`epic: db`** — Neon PostgreSQL, SQLModel Schemas & Alembic Pipeline
3. **`epic: historic data`** — CSV Parsing, Pydantic Adapter & Data Normalization
4. **`epic: ml`** — Feature Engineering, Model Training & Artifact Serialization
5. **`epic: api`** — Lunch Flow REST API Asynchronous Integration & Deduplication
6. **`epic: categorisation`** — Multi-Tier Engine (Rules $\rightarrow$ ML $\rightarrow$ LLM Fallback)
7. **`epic: ui`** — FastAPI Dashboard, HTMX Components & Chart Visualizations
8. **`epic: auth`** — Google OAuth 2.0 & Single-Email Whitelist Middleware
9. **`epic: infra`** — Docker Containerization, Terraform IaC & AWS Lambda Deployment

---

## 🚀 Local Development Setup

### Prerequisites
- Python 3.11+
- PostgreSQL (or Neon.tech connection string)
- Git

### Initial Workspace Setup

1. **Clone Repository & Initialize Virtual Environment:**
   ```bash
   git clone <repo-url>
   cd finance-tracker
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
# Product Steering: Serverless Personal Finance Tracker

## Purpose & Goal
An end-to-end, serverless personal finance application designed for personal use and portfolio demonstration. The primary objective is to build a robust system that ingests, cleanses, categorizes, and visualizes multi-bank transactions automatically at **zero cloud infrastructure cost**.

## Target Persona & Intent
- **Developer Intent:** The developer is acting as "Tech Lead" to master full-stack software engineering, data pipeline design, and serverless AWS architectures.
- **AI Persona Role:** Kiro acts as a **Senior Tech Lead & Code Reviewer**. Kiro must evaluate code for correctness, type safety, security, and cleanliness rather than simply outputting complete solutions without explanation.

## Core Features
1. **Multi-Bank Ingestion:** Normalizes historical CSV statements and live bank transaction feeds (Lunch Flow API).
2. **Multi-Tier Categorization Engine:**
   - Tier 0: Rule-based cross-account internal transfer filtering.
   - Tier 1: Machine learning model inference (`scikit-learn` / custom pipeline).
   - Tier 2: LLM API fallback for low-confidence predictions (< 0.70 confidence).
   - Tier 3: Manual override queue with feedback loop appending to training dataset.
3. **Interactive Dashboard:** Fast, responsive UI built with Jinja2, HTMX, Tailwind CSS, and Chart.js.
4. **Zero-Cost Deployment:** Serverless architecture hosted on AWS Lambda (compute), Neon (Postgres), API Gateway, and EventBridge (scheduling).
# 📈 Progress Tracker

> **Purpose:** our single source of truth. Read this at the start of every session to resume exactly where we left off.
> Full plan → [ROADMAP.md](ROADMAP.md)

---

## 🎯 Goals
1. Switch careers from **MEAN Stack Developer → Data Engineer** (with strong **Data Analytics** skills).
2. Master fundamentals in simple terms: Python, SQL, Pandas, statistics, data modeling, pipelines, Spark, Kafka, Cloud.
3. Build a portfolio of 6 projects + **1 real-time capstone app** in this repo.
4. Become interview-ready: SQL, Python, DE system design, concepts, and behavioral rounds.
5. Commit after each lesson and push after each milestone to `github.com/prasad1101/data-workspace`.

---

## 📍 Current Status
| Field | Value |
|---|---|
| **Current phase** | Phase 0: Setup & Foundations |
| **Current lesson** | 0.3: PostgreSQL in Docker (fixes pending) |
| **Next action** | Fix `first_queries.sql`: clean up duplicate rows, make the file safe to re-run, add ORDER BY and the 2 "Your turn" queries. Then say **"review"** → M0 |
| **Last updated** | 2026-11-09 |
| **Blockers / questions** | — |

---

## 🏁 Milestones
| # | Milestone | Status | Completed on |
|---|---|---|---|
| M-plan | Roadmap + repo created | ✅ Done | 2026-11-09 |
| M0 | Setup & Foundations | 🟡 In progress | |
| M1 | Python for Data + Project P1 (API → CSV ETL) | ⬜ Not started | |
| M2 | SQL Mastery + Project P2 (E-commerce SQL analytics) | ⬜ | |
| M3 | Pandas & NumPy + Project P3 (EDA report) | ⬜ | |
| M4 | Stats, Viz & BI + Project P4 (Dashboard) → *Analyst-ready* | ⬜ | |
| M5 | Data Modeling & Warehousing (dbt) | ⬜ | |
| M6 | Pipelines with Airflow + Project P5 (Batch ELT) | ⬜ | |
| M7 | Spark / PySpark + Project P6 | ⬜ | |
| M8 | Streaming with Kafka | ⬜ | |
| M9 | Cloud (AWS) | ⬜ | |
| M10 | Real-time Capstone App | ⬜ | |
| M11 | Interview & Job Prep → *Job-ready* 🎉 | ⬜ | |

---

## ✅ Lesson Checklist (current phase)
### Phase 0: Setup & Foundations
- [x] 0.1 Install `uv`, create a Python 3.12 virtual env, install Jupyter + Pandas
- [x] 0.2 Run the first notebook (`00-setup/hello_data.ipynb`): **score 9/10**
- [~] 0.3 Start PostgreSQL in Docker and connect with `psql` (Docker + VS Code extension working; SQL file needs fixes): **6/10 so far**
- [x] 0.4 Understand how data flows through a company (quiz): **7/10**
- [ ] 0.5 Commit + push → **M0 complete**

---

## 🧠 Review Notes / Weak Areas
*(I'll add feedback from code reviews here so we can revisit weak spots.)*
- **0.2 notebook (9/10):** all tasks correct, including the challenges. To fix: `orders = orders = [` typo; leave `df` as a cell's last line instead of `print(df)` for a nicer table. Learn next: `df.nlargest()`, `df.query()`.
- **0.3 SQL (6/10 so far):** running the file 4 times inserted the rows 4 times (12 rows). First lesson in **idempotency**. Missing: ORDER BY, the 2 "Your turn" queries.
- **0.4 quiz (7/10):** strong on OLTP vs OLAP and the roles. Weak: *why* ELT won (cloud compute, keeping raw data), streaming examples, lake = files of any format (not a DB). Model answers: `interview-prep/00-data-fundamentals.md`.

## 💼 Interview Readiness (self-rating 1–5, updated each milestone)
| Area | Rating | Notes |
|---|---|---|
| SQL | 1 | |
| Python (data) | 1 | knows JS well, so the jump is small |
| Statistics / A-B testing | 1 | |
| Data modeling | 1 | knows MongoDB (OLTP) |
| Pipelines / Airflow / dbt | 1 | |
| Spark | 1 | |
| Kafka / streaming | 1 | knows event-driven Node |
| Cloud (AWS) | 1 | |
| DE system design | 1 | |

---

## 🗒️ Session Log
| Date | What we did | Next |
|---|---|---|
| 2026-11-09 | Created the roadmap, progress tracker, repo structure and the Phase 0 lesson. First commit. | Do Phase 0 setup tasks |
| 2026-11-09 | Finished Parts A–C (venv, packages, first notebook). Notebook reviewed: 9/10. | Part D (Docker + Postgres) and Part E (quiz) |
| 2026-11-09 | Fixed a port clash (Docker Postgres moved to 5433), installed the VS Code PostgreSQL extension, reviewed the SQL file (6/10) and quiz (7/10). | Fix SQL file → M0 |

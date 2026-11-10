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
| **Current phase** | Phase 1: Python, Complete (syllabus: `01-python/README.md`) |
| **Current lesson** | 1.1: Python Basics (`01-python/01-basics/`) |
| **Next action** | Read `notes.md`, then do `exercises.md` Parts A–E (REPL, playground, quiz, `check.py` 13/13, receipt) → say **"review"** |
| **Last updated** | 2026-11-09 |
| **Blockers / questions** | — |

---

## 🏁 Milestones
| # | Milestone | Status | Completed on |
|---|---|---|---|
| M-plan | Roadmap + repo created | ✅ Done | 2026-11-09 |
| M0 | Setup & Foundations | ✅ Done | 2026-11-09 |
| M1 | Python Complete (20 lessons incl. FastAPI) + Project P1 (API → Postgres ETL + FastAPI service) | 🟡 In progress | |
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
- [x] 0.3 Start PostgreSQL in Docker and connect with `psql`: **8.5/10** after fixes (file is now idempotent)
- [x] 0.4 Understand how data flows through a company (quiz): **7/10**
- [x] 0.5 Commit + push → **M0 complete** ✅

### Phase 1: Python, Complete
- [ ] 1.1 Basics: variables, numbers, strings, booleans
- [ ] 1.2 Control flow
- [ ] 1.3 Lists, tuples, sets
- [ ] 1.4 Dictionaries & collections
- [ ] 1.5 Comprehensions & functional Python
- [ ] 1.6 Functions deep dive
- [ ] 1.7 Strings & text processing (regex)
- [ ] 1.8 Files, paths & data formats (CSV/JSON)
- [ ] 1.9 Errors, exceptions, logging & debugging
- [ ] 1.10 Modules, packages, environments & CLIs
- [ ] 1.11 OOP
- [ ] 1.12 Iterators, generators, decorators, context managers
- [ ] 1.13 Dates & times
- [ ] 1.14 Working with APIs
- [ ] 1.15 Databases from Python
- [ ] 1.16 Type hints, Pydantic & code quality
- [ ] 1.17 Testing with pytest
- [ ] 1.18 Performance & concurrency (async)
- [ ] 1.19 Building data APIs with FastAPI
- [ ] 1.20 Python interview mastery
- [ ] Project P1: API → Postgres ETL + FastAPI data service → **M1**

---

## 🧠 Review Notes / Weak Areas
*(I'll add feedback from code reviews here so we can revisit weak spots.)*
- **0.2 notebook (9/10):** all tasks correct, including the challenges. To fix: `orders = orders = [` typo; leave `df` as a cell's last line instead of `print(df)` for a nicer table. Learn next: `df.nlargest()`, `df.query()`.
- **0.3 SQL (8.5/10 final):** first version wasn't idempotent (rows duplicated on each run), fixed with `TRUNCATE ... RESTART IDENTITY` before the INSERT ✅. Took 2 rounds to apply all instructions, so read the task list carefully. Small gap: the plain "all products sorted by total" query was merged into the filter query instead of kept separate. **Revisit idempotency (upserts, `ON CONFLICT`) in Phase 2.**
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
| 2026-11-09 | SQL file fixed and verified idempotent (4 runs → still 3 rows, revenue 151000). **M0 complete.** | Start Phase 1: Python |
| 2026-11-10 | Prasad asked for full basics → advanced depth in every phase, plus FastAPI. Wrote the 20-lesson Phase 1 syllabus and Lesson 1.1 (detailed notes, exercises, auto-checker). Roadmap now ~40 weeks. | Do Lesson 1.1 |

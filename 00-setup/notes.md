# Phase 0: Setup & Foundations

## 1. How data flows in a company (the big picture)

Imagine your MEAN e-commerce app. Every order is saved in MongoDB. That's great for the **app**, but the CEO asks:
*"What was our revenue per city last month, and which products are trending?"*

Running heavy reports on the production DB would slow the app down. So companies build a **data platform**:

```
 SOURCES            INGESTION          STORAGE              TRANSFORM           SERVE
 ─────────          ─────────          ───────              ─────────           ─────
 MongoDB (app)  ─┐                    Data Lake (S3,        dbt / Spark /       BI dashboards
 MySQL/Postgres ─┼─► Batch (Airflow)─► raw files, Parquet)─► SQL: clean, join,─► (Power BI)
 APIs (Stripe)  ─┤   Stream (Kafka)    Data Warehouse        aggregate           ML models
 Logs/clicks    ─┘                     (Snowflake/Redshift)                      Reverse ETL
                └──────────── Data Engineer builds this ─────────┘  └─ Data Analyst uses this ─┘
```

- **Data Engineer** = builds and maintains the pipes (reliable, scalable, tested).
- **Data Analyst** = uses the clean data to answer questions and build dashboards.

### Key words (you'll hear these in every interview)
| Term | Simple meaning |
|---|---|
| **ETL** | Extract → Transform → Load (clean *before* loading into the warehouse) |
| **ELT** | Extract → Load → Transform (load raw first, transform *inside* the warehouse; the modern approach) |
| **Batch** | Process data in chunks on a schedule (e.g. every night at 2 AM) |
| **Streaming** | Process each event as it happens (e.g. fraud detection in seconds) |
| **OLTP** | Database for the app: many small reads/writes (MongoDB, Postgres behind your API) |
| **OLAP** | Database for analysis: few, huge, read-heavy queries (Redshift, BigQuery, Snowflake) |
| **Data Lake** | Cheap storage for raw files of any format (S3) |
| **Data Warehouse** | Structured, cleaned tables optimized for SQL analytics |
| **Pipeline** | Automated series of steps that moves/transforms data |

## 2. Python environment (like `node_modules`, but for Python)

| Node world | Python world |
|---|---|
| `nvm` (Node versions) | `uv python install` / `pyenv` |
| `npm` / `package.json` | `uv` or `pip` / `pyproject.toml` / `requirements.txt` |
| `node_modules/` (per project) | `.venv/` (virtual environment, per project) |
| `npx` | `uv run` |

We use **`uv`**: a very fast, modern Python package manager (think `pnpm` for Python).
We use **Python 3.12** instead of your system 3.14, because data tools (Airflow, PySpark) lag behind the newest Python.

## 3. Jupyter notebooks
A notebook is like a **REPL with memory + markdown + charts**, saved as a file. Analysts live in notebooks.
Engineers write `.py` modules for production, and use notebooks for exploration.
VS Code opens `.ipynb` files natively (install the *Python* and *Jupyter* extensions).

## 4. PostgreSQL in Docker
We'll do all SQL learning in Postgres (the most interview-friendly SQL dialect).
`00-setup/docker-compose.yml` starts it with one command, just like you may have done for MongoDB.

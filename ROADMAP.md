# 🗺️ Roadmap: MEAN Stack Developer → Data Engineer / Data Analyst

> **Goal:** Become a job-ready, interview-proof Data Engineer who can also do Data Analytics.
> **Pace assumed:** ~10–12 hrs/week (≈ 1.5 hrs on weekdays + some weekend time). **Total: ~40 weeks.** Week numbers below are approximate.
> **Depth standard:** every phase covers its topics completely: basics → intermediate → advanced → interview level, so you never need a separate course. Each phase folder has a `README.md` with the full syllabus.
> Faster or slower is fine — the *milestones* matter, not the dates.

---

## 0. First, understand the roles (in simple words)

| Role | What they do every day | Main tools | Analogy for a web dev |
|---|---|---|---|
| **Data Analyst** | Answers business questions with data: "Why did sales drop in March?" | SQL, Excel, Python (Pandas), Power BI/Tableau, statistics | Like a dev who builds the *reports page*, but also figures out what the numbers mean |
| **Data Engineer** | Builds the *pipes* that move, clean and store data so analysts/ML can use it | SQL, Python, Spark, Airflow, dbt, Kafka, Cloud (AWS/GCP), Docker | Like a backend dev — but instead of APIs serving users, you build pipelines serving data |
| **Data Scientist** | Builds predictive models (ML) | Python, statistics, scikit-learn | Not our main target, but we'll touch the basics |

**Your advantage as a MEAN developer:** you already know programming, Git, APIs, JSON, MongoDB, Node, Docker-ish workflows, debugging. Most career-switchers struggle with *those*. You mainly need: **SQL depth, Python data stack, data modeling, pipelines, and big-data/cloud tools.**

---

## 1. How every topic will work (our learning loop)

```
 ① LEARN    → I explain the concept in simple language + a JavaScript comparison
 ② EXAMPLE  → Runnable code / SQL you can play with
 ③ TASK     → Exercises in the topic folder (exercises.md + your solution files)
 ④ REVIEW   → You say "review" → I check your code, give feedback + a score
 ⑤ QUIZ     → 5–10 interview-style questions on the topic
 ⑥ COMMIT   → Milestone done → update progress.md → git commit + push
```

**Rules we follow**
- You write the solutions; I guide and review (no copy-paste learning 🙂).
- Every phase ends with a **mini project** that goes on your GitHub/resume.
- `progress.md` is always updated, so no context is ever lost between sessions.
- Interview prep runs **in parallel from week 5** (1 SQL problem a day), not just at the end.

---

## 2. The Phases

### 🧰 Phase 0 — Setup & Foundations (Week 1)
- Python 3.12 virtual environment (using `uv`), VS Code + Jupyter
- Git workflow for this repo (commit after each milestone)
- Docker basics refresh (we'll run PostgreSQL, Airflow, Kafka in Docker)
- How data flows in a company: sources → ingestion → storage → transformation → BI/ML
- **Milestone M0:** environment works, first notebook runs, first commit pushed ✅

### 🐍 Phase 1 — Python, Complete (Weeks 2–7) · full syllabus: [01-python/README.md](01-python/README.md)
20 lessons from basics to advanced (OOP, generators, decorators, async, testing, type hints) + **FastAPI** for building data APIs.
| Topic | Simple idea | JS comparison |
|---|---|---|
| Syntax, types, f-strings | Python basics | `let x = 5` → `x = 5` |
| Lists, dicts, sets, tuples | Core data structures | Array, Object, Set, frozen array |
| Comprehensions | One-line loops | `arr.map().filter()` |
| Functions, `*args`, `**kwargs`, lambdas | Reusable logic | Rest/spread params, arrow functions |
| Modules, packages, venv, pip | Code organization | `require`/`import`, `npm`, `node_modules` |
| File I/O: CSV, JSON, Excel | Reading/writing data | `fs.readFile` |
| Error handling, logging | Robust scripts | `try/catch` |
| OOP: classes, dataclasses | Modeling things | ES6 classes |
| Iterators, generators | Process huge files lazily | Generators / streams |
| APIs with `requests` | Pull data from the web | `axios`/`fetch` |
| Type hints, testing (pytest) | Production-quality code | TypeScript, Jest |

- **Mini-project P1:** *API → CSV ETL script* — pull data from a public API, clean it, save it as CSV/JSON, with logging + tests.
- **Milestone M1** ✅

### 🗄️ Phase 2 — SQL Mastery (Weeks 5–8) ⭐ *Most important for interviews*
PostgreSQL in Docker with a realistic e-commerce dataset.
1. SELECT, WHERE, ORDER BY, LIMIT, DISTINCT
2. Aggregations: COUNT/SUM/AVG, GROUP BY, HAVING
3. JOINs: inner, left, right, full, self, cross (with Venn + row-level examples)
4. Subqueries & CTEs (`WITH`), recursive CTEs
5. **Window functions**: ROW_NUMBER, RANK, DENSE_RANK, LAG/LEAD, running totals, moving averages
6. CASE, COALESCE, string/date functions
7. DDL/DML, constraints, transactions, ACID
8. Normalization (1NF–3NF) vs denormalization — vs MongoDB documents you know
9. Indexes, `EXPLAIN ANALYZE`, query optimization
10. Views, materialized views, stored procedures (basics)

- **Interview drill:** 60+ classic problems (2nd highest salary, top-N per group, consecutive days, retention, funnel, YoY growth, gaps & islands…)
- **Mini-project P2:** *E-commerce analytics in SQL* — 20 business questions answered with SQL.
- **Milestone M2** ✅

### 🐼 Phase 3 — Data Analysis with NumPy & Pandas (Weeks 9–11)
- NumPy arrays, vectorization (why loops are slow)
- Pandas: Series/DataFrame, reading data, selecting, filtering
- Cleaning: missing values, duplicates, types, outliers, string cleanup
- `groupby`, `merge`/`join`, `pivot_table`, `melt`, apply/map
- Time series: datetime, resampling, rolling windows
- Pandas ↔ SQL side-by-side (you'll see they are the same ideas)
- Performance: Parquet, chunking, intro to **Polars** and **DuckDB**
- **Mini-project P3:** *EDA on a real dataset* (e.g. NYC taxi / Airbnb / Olist e-commerce) with a written insights report.
- **Milestone M3** ✅

### 📊 Phase 4 — Statistics, Visualization & BI (Weeks 12–13)
- Descriptive stats: mean, median, mode, variance, std dev, percentiles
- Distributions (normal, skewed), correlation ≠ causation
- Sampling, confidence intervals, hypothesis testing, p-values (in plain English)
- **A/B testing** (very common analyst interview topic)
- Analytics metrics: DAU/MAU, retention, churn, cohorts, funnels, LTV
- Visualization: Matplotlib, Seaborn, Plotly — choosing the right chart
- BI tool: **Power BI** (or Metabase/Superset — free & Docker-friendly)
- Excel/Google Sheets essentials for analysts: pivot tables, XLOOKUP, conditional formatting
- **Mini-project P4:** *Interactive business dashboard* on the P3 dataset.
- **Milestone M4** ✅ → *At this point you are ready for Data Analyst interviews.*

### 🏛️ Phase 5 — Data Modeling & Warehousing (Weeks 14–15)
- OLTP vs OLAP (your MongoDB/MEAN apps = OLTP)
- Dimensional modeling (Kimball): facts, dimensions, **star vs snowflake schema**
- Slowly Changing Dimensions (SCD Type 1, 2)
- Data warehouse vs data lake vs **lakehouse**; columnar storage
- Snowflake / BigQuery / Redshift concepts
- **dbt**: models, tests, docs, incremental models
- **Milestone M5** ✅

### ⚙️ Phase 6 — Data Engineering Core: Pipelines (Weeks 16–19)
- ETL vs ELT, batch vs streaming, idempotency, backfills
- File formats: CSV vs JSON vs **Parquet** vs Avro; partitioning; compression
- **Apache Airflow**: DAGs, operators, scheduling, retries, sensors, XCom
- Data quality: Great Expectations / dbt tests, data contracts
- Docker Compose for data stacks
- Logging, monitoring, alerting for pipelines
- **Project P5 (portfolio-grade):** *Batch ELT pipeline* — API/DB source → Airflow → raw layer → dbt → star schema in Postgres/DuckDB → dashboard.
- **Milestone M6** ✅

### 🔥 Phase 7 — Big Data with Apache Spark (Weeks 20–22)
- Why distributed computing; Hadoop/HDFS in 1 lesson (history + concepts)
- Spark architecture: driver, executors, partitions, lazy evaluation, DAG
- PySpark DataFrames & Spark SQL
- Joins at scale: shuffle, broadcast joins, skew, partitioning, caching
- Performance tuning (top interview topic)
- Delta Lake / Apache Iceberg basics; Databricks overview
- **Mini-project P6:** process a multi-GB dataset with PySpark → partitioned Parquet/Delta.
- **Milestone M7** ✅

### ⚡ Phase 8 — Streaming & Real-Time (Weeks 23–24)
- Event-driven architecture (you know this from Node!)
- **Apache Kafka**: topics, partitions, producers, consumers, consumer groups, offsets
- Spark Structured Streaming (or Flink intro): windows, watermarks, exactly-once
- Change Data Capture (Debezium) concept
- **Milestone M8** ✅

### ☁️ Phase 9 — Cloud Data Engineering (Weeks 25–26)
- AWS (most job openings): S3, IAM, Glue, Athena, Redshift, Lambda, EMR — on free tier
- Infrastructure basics (Terraform intro), cost awareness
- Alternatives at a glance: GCP (BigQuery, Dataflow), Azure (ADF, Synapse), Snowflake, Databricks
- **Milestone M9** ✅

### 🚀 Phase 10 — Capstone Real-Time App (Weeks 27–28)
**"Live E-commerce Analytics Platform"** (built in `projects/realtime-capstone/`)
```
 Order generator (Node.js — your strength)
        │  events
        ▼
     Kafka  ──►  Spark Structured Streaming / Python consumer
                         │  aggregates (revenue/min, top products, fraud flags)
                         ▼
            PostgreSQL / ClickHouse  +  S3/Parquet (history)
                         │
                         ▼
   FastAPI (REST + WebSockets) ──► Live dashboard (Angular) or Grafana/Superset
        + Airflow nightly batch job + dbt models for historical reports
```
Fully Dockerized, documented README with architecture diagram — your **flagship resume project**.
- **Milestone M10** ✅

### 🎯 Phase 11 — Interview & Job Prep (Weeks 29–30, plus ongoing)
- SQL: timed mock rounds (medium/hard)
- Python: data-structure & Pandas coding rounds
- **Data engineering system design**: "Design a pipeline for X", batch vs streaming trade-offs, scaling, failure handling
- Concept rapid-fire: 150+ Q&A in `interview-prep/` (built up through every phase)
- Behavioral (STAR method) + "why switch from MEAN to data?" story
- Resume rewrite (MEAN experience reframed for data), LinkedIn, GitHub polish
- Mock interviews with me
- **Milestone M11** ✅ → 🎉 Job-ready

---

## 3. Folder structure (grows as we go)

```
data-workspace/
├── README.md            # repo overview
├── ROADMAP.md           # this plan
├── progress.md          # goals + current status + log (our memory)
├── 00-setup/
├── 01-python/
├── 02-sql/
├── 03-pandas/
├── 04-stats-viz/
├── 05-data-modeling/
├── 06-pipelines/
├── 07-spark/
├── 08-streaming/
├── 09-cloud/
├── projects/            # P1…P6 + realtime-capstone
└── interview-prep/      # sql-problems, concepts Q&A, system design, behavioral
```
Each topic folder contains: `notes.md` (lesson), `exercises.md` (tasks), and your solution files.

## 4. Git conventions
- Commit after each lesson: `lesson(01-python): comprehensions exercises`
- Commit + **push** after each milestone: `milestone(M1): Python for Data complete`
- Never commit: virtualenvs, big datasets, secrets/`.env` (handled by `.gitignore`)

## 5. Free resources we'll lean on (optional extra reading)
- SQL practice: LeetCode SQL 50, DataLemur, StrataScratch
- Pandas: official "10 minutes to pandas"
- DE: DataTalksClub *Data Engineering Zoomcamp* (free, excellent)
- Books (later): *Fundamentals of Data Engineering* (Reis & Housley), *The Data Warehouse Toolkit* (Kimball), *Designing Data-Intensive Applications* (Kleppmann)

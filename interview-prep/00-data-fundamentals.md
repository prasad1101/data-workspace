# Interview Q&A: Data Fundamentals (Phase 0)

> Model answers. Practise saying them out loud in about 30–60 seconds each.

### 1. What's the difference between a Data Engineer and a Data Analyst?
A **Data Engineer** builds and maintains the infrastructure that moves data from source systems (app databases, APIs, logs) into storage like a data lake or warehouse. They make it reliable, automated, tested and scalable.
A **Data Analyst** uses that clean data to answer business questions. They write SQL, build dashboards and reports, and explain trends to stakeholders.
*One-liner:* engineers build the roads, analysts drive on them to reach insights.

### 2. ETL vs ELT: which is more common today and why?
- **ETL:** transform the data *before* loading it into the warehouse. This was common when warehouse storage and compute were expensive.
- **ELT:** load the raw data first, then transform it *inside* the warehouse with SQL (often using dbt). **ELT is more common today** because:
  1. Cloud warehouses (Snowflake, BigQuery, Redshift) have cheap storage and compute that scales.
  2. Keeping the raw data means you can re-run transformations when business logic changes, or recover from bugs.
  3. Transformations are written in SQL, so analysts can contribute (the "analytics engineer" role).
  4. Loading is faster and simpler. New sources can land quickly before anyone decides how to model them.

### 3. Is an app's MongoDB OLTP or OLAP? Why not run the yearly report on it?
It's **OLTP** (Online Transaction Processing). It's optimized for many small, fast reads and writes, like creating an order or fetching one user.
A yearly report scans millions of rows. On the production database that:
- competes for CPU, memory and disk with real users, so the app slows down or even times out
- uses a data layout (row/document storage, indexes built for lookups) that is poor for big aggregations
- often lacks history (data is updated in place) and lacks data from other sources (payments, marketing)

So we copy the data into an **OLAP** system (a warehouse with columnar storage) that is built for large analytical queries.

### 4. Give batch and streaming examples in e-commerce
- **Batch** (scheduled, e.g. nightly): daily sales report, best-selling products today, monthly invoices, refreshing the recommendation model.
- **Streaming** (seconds, event by event): **fraud detection on a payment**, live inventory updates ("only 2 left"), real-time delivery tracking, live sales dashboard during a flash sale, abandoned-cart notifications.
*Rule of thumb:* if a decision loses value within seconds or minutes, use streaming. Otherwise batch is simpler and cheaper.

### 5. Data lake vs data warehouse?
| | Data Lake | Data Warehouse |
|---|---|---|
| What | Cheap file/object storage (S3, ADLS, GCS) | Database optimized for analytics (Snowflake, BigQuery, Redshift) |
| Data | Raw data in **any format**: CSV, JSON, Parquet, images, logs | **Structured**, cleaned, modeled tables |
| Schema | **Schema-on-read** (structure applied when you query) | **Schema-on-write** (structure enforced when you load) |
| Users | Data engineers, data scientists | Analysts, BI tools |
| Cost | Very cheap | More expensive per GB |

**Bonus term, lakehouse:** table formats (Delta Lake, Apache Iceberg) add warehouse features such as ACID transactions and schema enforcement on top of cheap lake storage. Databricks is the best-known example.

### Bonus: What is idempotency, and why does it matter in pipelines?
A job is **idempotent** if running it once or many times gives the same result.
Pipelines get retried after failures and re-run for backfills, so they must not create duplicate data.
Common techniques: delete or overwrite the partition before writing, `TRUNCATE` + load, `INSERT ... ON CONFLICT DO NOTHING/UPDATE` (upsert), or `MERGE`.

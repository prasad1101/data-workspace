# Phase 0: Exercises

Run all commands from the repo root: `/Users/ankitapawar/prasad/data-workspace`

## Task 0.1: Python environment
```bash
brew install uv                      # install uv
uv python install 3.12               # get Python 3.12 (like nvm install)
uv venv --python 3.12                # creates .venv/ in the repo
source .venv/bin/activate            # activate it (prompt shows (.venv))
uv pip install jupyter pandas numpy matplotlib requests sqlalchemy psycopg2-binary
uv pip freeze > requirements.txt     # like package-lock.json
python --version                     # should print 3.12.x
```
✅ Done when `python --version` shows 3.12 inside the venv.

## Task 0.2: Your first notebook
1. In VS Code install the **Python** and **Jupyter** extensions.
2. Create `00-setup/hello_data.ipynb` and select the `.venv` kernel (top right).
3. In cells, write code that:
   - creates a Python list of 5 dicts, e.g. `{"product": "Laptop", "price": 55000, "qty": 2}`
     (yes, it's exactly like a JS array of objects)
   - turns it into a Pandas DataFrame: `import pandas as pd; df = pd.DataFrame(orders)`
   - adds a column `total = price * qty`
   - prints the total revenue and the most expensive product
   - draws a bar chart of total per product: `df.plot.bar(x="product", y="total")`
4. Add one markdown cell explaining in your own words what you did.

Don't worry if Pandas feels new; try it, guess, and Google. That's the point.

## Task 0.3: PostgreSQL in Docker
```bash
docker compose -f 00-setup/docker-compose.yml up -d
psql -h localhost -U learner -d playground      # password: learner
```
Inside psql, run:
```sql
CREATE TABLE orders (id SERIAL PRIMARY KEY, product TEXT, price NUMERIC, qty INT);
INSERT INTO orders (product, price, qty) VALUES ('Laptop', 55000, 2), ('Mouse', 500, 10), ('Monitor', 12000, 3);
SELECT product, price * qty AS total FROM orders ORDER BY total DESC;
```
Save the SQL you ran in `00-setup/first_queries.sql`.

## Task 0.4: Concept quiz (answer in `00-setup/quiz_answers.md`)
1. In your own words, what's the difference between a Data Engineer and a Data Analyst?
2. ETL vs ELT: which is more common today, and why?
3. Your MEAN app's MongoDB: is it OLTP or OLAP? Why shouldn't the CEO's yearly report run directly on it?
4. Give one example each of a **batch** and a **streaming** use case in an e-commerce company.
5. What is a data lake vs a data warehouse?

## When you're done
Say **"review setup"** in chat. I'll review your notebook, SQL and quiz answers, then we commit and push M0 and start Phase 1 (Python).

# Phase 0: Step-by-Step Setup Guide (absolute beginner version)

> Follow the steps **in order**. Each step shows **what to do**, **what it means**, and **what you should see**.
> If anything looks different from "✅ You should see", stop and paste the error into the chat.

---

## PART A: Open the project

### Step 1: Open the folder in VS Code
1. Open **Visual Studio Code**.
2. Menu **File → Open Folder…** → select `/Users/ankitapawar/prasad/data-workspace` → **Open**.
3. On the left (Explorer) you should see: `00-setup`, `ROADMAP.md`, `progress.md`, `README.md`.

### Step 2: Open the terminal inside VS Code
- Menu **Terminal → New Terminal** (shortcut: `` Ctrl + ` ``).
- A panel opens at the bottom. Type this and press Enter:
```bash
pwd
```
✅ You should see: `/Users/ankitapawar/prasad/data-workspace`
> 💡 `pwd` = "print working directory": it tells you which folder you're in. Like `process.cwd()` in Node.

---

## PART B: Python environment (Task 0.1)

### Step 3: Install `uv` (Python's "npm")
```bash
brew install uv
uv --version
```
✅ You should see something like `uv 0.x.x`

### Step 4: Install Python 3.12
```bash
uv python install 3.12
```
✅ You should see: `Installed Python 3.12.x`
> 💡 Like `nvm install 20`. Your Mac already has Python 3.14, but data tools work best on 3.12.

### Step 5: Create the virtual environment
```bash
uv venv --python 3.12
```
✅ You should see: `Creating virtual environment at: .venv`
> 💡 `.venv/` is like `node_modules/`: all the packages for **this project only** live there. It's in `.gitignore`, so it's never committed.

### Step 6: Activate the environment
```bash
source .venv/bin/activate
```
✅ Your prompt now starts with `(data-workspace)` or `(.venv)`.
> ⚠️ **Every time you open a new terminal you must run this again.** If the prompt prefix is missing, your packages "disappear".

Check it worked:
```bash
python --version
```
✅ You should see: `Python 3.12.x`

### Step 7: Install the data packages
```bash
uv pip install jupyter ipykernel pandas numpy matplotlib requests sqlalchemy psycopg2-binary
uv pip freeze > requirements.txt
```
✅ You should see a list of installed packages, and a new file `requirements.txt` appears on the left.
> 💡 `requirements.txt` is like `package-lock.json`. Anyone can recreate your setup with `uv pip install -r requirements.txt`.

| Package | What it does |
|---|---|
| `pandas` | Tables of data in Python (like Excel inside code) |
| `numpy` | Fast math on arrays |
| `matplotlib` | Charts |
| `jupyter`, `ipykernel` | Notebooks |
| `requests` | Call APIs (like axios) |
| `sqlalchemy`, `psycopg2-binary` | Connect Python to PostgreSQL |

---

## PART C: Your first notebook (Task 0.2)

### Step 8: Install the VS Code extensions
1. Press `Cmd + Shift + X` (Extensions panel).
2. Search **Python** → install the one by **Microsoft**.
3. Search **Jupyter** → install the one by **Microsoft**.

### Step 9: Tell VS Code to use your `.venv`
1. Press `Cmd + Shift + P` → type **Python: Select Interpreter** → press Enter.
2. Choose the one that shows **`.venv`** and **3.12**.

### Step 10: Create the notebook
1. In the Explorer, right-click the **00-setup** folder → **New File…** → name it `hello_data.ipynb`.
2. The notebook opens. Top right, click **Select Kernel** → **Python Environments** → choose **.venv (3.12)**.
3. You'll see a cell (a box). Type code in it and press **`Shift + Enter`** to run it. A new cell appears below.
4. To add a text (markdown) cell, hover between cells and click **+ Markdown**.

### Step 11: Type these cells one by one (type them, don't paste; typing builds memory)

**Cell 1: create data (a list of dictionaries = a JS array of objects)**
```python
orders = [
    {"product": "Laptop",   "price": 55000, "qty": 2},
    {"product": "Mouse",    "price": 500,   "qty": 10},
    {"product": "Monitor",  "price": 12000, "qty": 3},
    {"product": "Keyboard", "price": 1500,  "qty": 5},
    {"product": "Headset",  "price": 2500,  "qty": 4},
]
print(orders[0])            # first item, like orders[0] in JS
print(len(orders))          # length, like orders.length
```
✅ Output: `{'product': 'Laptop', 'price': 55000, 'qty': 2}` and `5`

**Cell 2: turn it into a table (a DataFrame)**
```python
import pandas as pd          # like: const pd = require("pandas")

df = pd.DataFrame(orders)
df
```
✅ You see a nice table with 5 rows and 3 columns.
> 💡 A **DataFrame** = a table (rows + columns). It's the #1 object in data work.

**Cell 3: add a calculated column**
```python
df["total"] = df["price"] * df["qty"]   # multiplies every row at once, no loop needed!
df
```
> 💡 In JS you'd write `orders.map(o => ({...o, total: o.price * o.qty}))`. Pandas does it in one line for millions of rows.

**Cell 4: answer questions**
```python
total_revenue = df["total"].sum()
print(f"Total revenue: ₹{total_revenue}")        # f-string = JS template literal `${}`

most_expensive = df.loc[df["price"].idxmax(), "product"]
print(f"Most expensive product: {most_expensive}")
```
✅ Output: `Total revenue: ₹189500` and `Most expensive product: Laptop`

**Cell 5: draw a chart**
```python
df.plot.bar(x="product", y="total", title="Revenue per product")
```
✅ A bar chart appears below the cell 🎉

### Step 12: 🧠 Your turn (small challenge; try it before asking me)
Add new cells that:
1. Print the product with the **highest total** (hint: same as Cell 4 but use the `"total"` column).
2. Show only rows where `qty > 3` (hint: `df[df["qty"] > 3]`, which is like `.filter()` in JS).
3. Sort the table by total, biggest first (hint: search "pandas sort_values descending").
4. Add a **Markdown cell** at the top that explains in 3–4 lines, in your own words, what this notebook does.

Press `Cmd + S` to save.

---

## PART D: PostgreSQL in Docker (Task 0.3)

### Step 13: Start Docker (Colima)
Your Mac runs Docker through **Colima** (a lightweight Docker engine). Start it:
```bash
colima start
```
⏳ The first time takes 2–5 minutes (it downloads a small Linux VM).
Check it:
```bash
docker ps
```
✅ You should see a header line `CONTAINER ID   IMAGE ...` (an empty list is fine).

### Step 14: Start PostgreSQL
```bash
docker compose -f 00-setup/docker-compose.yml up -d
docker ps
```
✅ You should see a container named **dw-postgres** with status `Up`.
> 💡 `-d` = run in the background (detached). The file `00-setup/docker-compose.yml` says "run Postgres 16, user `learner`, password `learner`, database `playground`".

### Step 15: Write your first SQL file
1. Create a new file `00-setup/first_queries.sql` and type:
```sql
-- 1. Create a table (like defining a Mongoose schema)
CREATE TABLE IF NOT EXISTS orders (
    id      SERIAL PRIMARY KEY,   -- auto-increment id (like Mongo's _id)
    product TEXT,
    price   NUMERIC,
    qty     INT
);

-- 2. Insert rows (like Model.insertMany([...]))
INSERT INTO orders (product, price, qty) VALUES
    ('Laptop', 55000, 2),
    ('Mouse', 500, 10),
    ('Monitor', 12000, 3);

-- 3. Query (like Model.find().sort())
SELECT product, price * qty AS total
FROM orders
ORDER BY total DESC;
```

### Step 16: Run the SQL file
```bash
export PGPASSWORD=learner
psql -h localhost -U learner -d playground -f 00-setup/first_queries.sql
```
✅ You should see `CREATE TABLE`, `INSERT 0 3`, and then a small table: Laptop 110000, Monitor 36000, Mouse 5000.

### Step 17: Play inside Postgres interactively
```bash
psql -h localhost -U learner -d playground
```
You're now "inside" the database (prompt `playground=#`). Try:
```sql
\dt                         -- list tables
SELECT * FROM orders;       -- see everything
SELECT COUNT(*) FROM orders;
\q                          -- quit
```
> ⚠️ Every SQL statement must end with `;`. If the prompt changes to `playground-#`, it's waiting for a `;`.

🧠 **Your turn:** add 2 queries at the bottom of `first_queries.sql`:
1. Show only orders where `qty >= 3`.
2. Show the total revenue of all orders (hint: `SUM(price * qty)`).

---

## PART E: Concept quiz (Task 0.4)
1. Re-read `00-setup/notes.md`.
2. Create `00-setup/quiz_answers.md` and answer **in your own words** (short is fine, wrong is fine, that's what review is for):
   1. What's the difference between a Data Engineer and a Data Analyst?
   2. ETL vs ELT: which is more common today, and why?
   3. Your MEAN app's MongoDB: is it OLTP or OLAP? Why shouldn't the CEO's yearly report run directly on it?
   4. Give one example each of a **batch** and a **streaming** use case in an e-commerce company.
   5. What is a data lake vs a data warehouse?

---

## PART F: Get reviewed and commit

### Step 18: Ask for a review
In the Claude chat, type: **`review setup`**

### Step 19: Commit (I'll guide you the first time, then you'll do it yourself)
```bash
git status                       # see what changed (red = not staged)
git add .                        # stage everything (.gitignore keeps .venv out)
git commit -m "milestone(M0): setup complete"
git push                         # send to GitHub
```
Open https://github.com/prasad1101/data-workspace to see your work online. 🎉

---

## 🌙 End of each study session
```bash
docker compose -f 00-setup/docker-compose.yml stop   # stop Postgres (your data is kept)
colima stop                                          # stop the Docker engine (frees RAM)
deactivate                                           # leave the Python venv
```
## ☀️ Start of each study session
```bash
cd /Users/ankitapawar/prasad/data-workspace
source .venv/bin/activate
colima start                                         # only if you need Postgres today
docker compose -f 00-setup/docker-compose.yml start
```

---

## 🆘 Troubleshooting
| Problem | Fix |
|---|---|
| `command not found: uv` | Run `brew install uv` again, then close and reopen the terminal |
| `ModuleNotFoundError: No module named 'pandas'` | The venv isn't active, or the notebook kernel isn't `.venv`. Re-do Step 6 / Step 10.2 |
| `Cannot connect to the Docker daemon` | Run `colima start` |
| `port 5432 already in use` | Another Postgres is running: `brew services stop postgresql` and retry Step 14 |
| `psql: password authentication failed` | Password is `learner`; or run `export PGPASSWORD=learner` first |
| Anything else | Copy the full error message and paste it in the chat |

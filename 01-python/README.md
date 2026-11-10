# Phase 1: Python, Complete (Basics → Advanced → Interview)

> **Goal:** after this phase you never need another Python course. You'll be able to write production-quality Python for data engineering and pass Python interview rounds.
> **Duration:** ~5–6 weeks at 10–12 hrs/week. Each lesson takes about 2–4 hours.

## How each lesson folder works
```
01-python/01-basics/
├── notes.md        ← read + type every example (detailed theory, JS comparisons, gotchas, interview Q&A)
├── exercises.md    ← step-by-step tasks, in order
├── playground.py   ← YOU create it: type the examples from notes here and run them
├── exercises.py    ← functions for YOU to complete
├── check.py        ← auto-checker: `python 01-python/01-basics/check.py` shows ✅ / ❌
└── quiz_answers.md ← YOU create it: predict-the-output + concept answers
```
**Lesson loop:** read notes → type examples → predict-output quiz → exercises until `check.py` is all ✅ → mini challenge → say **"review"** → commit.

---

## Syllabus (✅ = lesson written, ⬜ = written when you reach it)

### 🟢 Level 1: Foundations
**✅ 1.1 Python Basics: variables, numbers, strings, booleans** (`01-basics/`)
How Python runs (interpreter, bytecode, REPL vs scripts) · `print` options · comments & docstrings · variables, dynamic + strong typing, naming rules · int (unlimited size), float, `/` `//` `%` `**`, negative floor division · float precision & `Decimal` for money · `round()` banker's rounding · `math` module · NaN & infinity · strings: indexing, slicing, immutability, 25+ methods, f-string format specs (`:,.2f`, `:>10`, `:.1%`, `=`) · escape & raw strings · booleans, `None`, truthiness (differs from JS!) · `and`/`or` return values · `is` vs `==` · type conversion & `isinstance` · `input()` · JS → Python cheat sheet

**⬜ 1.2 Control Flow**
`if/elif/else` · nested conditions · ternary expression · `match/case` (structural pattern matching) · `for` + `range` · `while` · `break`/`continue`/`pass` · loop `else` clause · `enumerate`, `zip`, `reversed`, `sorted` · walrus operator `:=` · common loop patterns (accumulator, counter, flag, min/max tracking)

**⬜ 1.3 Lists, Tuples, Sets**
List methods (append, extend, insert, pop, remove, sort, reverse, index, count) · slicing & slice assignment · `sort()` vs `sorted()` with `key=` and `reverse=` · copying: references, shallow vs deep copy (`copy` module) · nested lists (matrices) · tuples & immutability · packing/unpacking, `*rest` · named tuples · sets: union, intersection, difference, symmetric difference, dedup · time complexity (O(1) vs O(n) membership)

**⬜ 1.4 Dictionaries & the `collections` module**
Create/read/update/delete · `get`, `setdefault`, `pop`, `update`, `|` merge · iterating `keys/values/items` · ordering guarantee · nested dicts (JSON-like data, like JS objects) · hashing & what can be a key · `Counter`, `defaultdict`, `OrderedDict`, `deque`, `ChainMap` · grouping & counting patterns (the core of data work) · dict ⇄ JSON

**⬜ 1.5 Comprehensions & Functional Python**
List/dict/set comprehensions · conditions & nested comprehensions · generator expressions (memory) · `map`, `filter`, `functools.reduce` · `lambda` · `any`, `all`, `min/max/sorted` with `key` · `itertools` basics · when NOT to use comprehensions

### 🟡 Level 2: Writing Real Programs
**⬜ 1.6 Functions Deep Dive**
`def`, `return`, multiple return values · positional, keyword, default arguments · the **mutable default argument trap** · `*args`, `**kwargs`, unpacking in calls · keyword-only `*` and positional-only `/` parameters · scope: LEGB, `global`, `nonlocal` · first-class functions, higher-order functions · closures & late-binding gotcha · recursion & recursion limit · docstrings · type hints intro

**⬜ 1.7 Strings & Text Processing (advanced)**
Unicode, `encode`/`decode`, UTF-8 vs others (fixing "garbled" CSV files) · string building performance (`join` vs `+=`) · **regular expressions** (`re`): patterns, groups, named groups, `findall`, `sub`, `split`, flags, greedy vs lazy · validating & extracting (emails, phones, dates, log lines) · `textwrap`, `string` module

**⬜ 1.8 Files, Paths & Data Formats**
`open()` modes, encodings, `with` · reading large files line by line · `pathlib` (modern paths) · `os`, `shutil`, `glob` · **CSV** (`csv.reader`, `DictReader`, `DictWriter`, dialects, quoting) · **JSON** (`load/loads/dump/dumps`, nested, pretty-print, custom encoders) · JSON Lines · Excel intro · Parquet preview · zip/gzip files · temp files

**⬜ 1.9 Errors, Exceptions, Logging & Debugging**
Exception hierarchy · `try/except/else/finally` · catching specific exceptions · `raise`, re-raise, exception chaining (`from`) · custom exception classes · EAFP vs LBYL style · `logging` module (levels, formatters, handlers, log files) · `warnings` · **VS Code debugger** (breakpoints, step, watch) · `pdb` · reading tracebacks

**⬜ 1.10 Modules, Packages, Environments & CLIs**
How `import` works, `sys.path` · `if __name__ == "__main__"` · creating packages, `__init__.py`, relative imports · `pyproject.toml`, `uv add`, dependency pinning · environment variables & `.env` (secrets!) · `argparse` command-line tools · project structure for data pipelines

**⬜ 1.11 Object-Oriented Programming**
Classes, objects, `__init__`, `self` (vs JS `this`) · instance vs class attributes · instance/class/static methods · encapsulation & `_private` convention · `@property` · inheritance, `super()`, method overriding, MRO · composition vs inheritance · **dunder methods** (`__repr__`, `__str__`, `__eq__`, `__lt__`, `__len__`, `__iter__`, `__getitem__`, `__enter__/__exit__`) · `@dataclass` (frozen, ordering, defaults) · abstract base classes · `Enum` · SOLID basics for pipelines

### 🔴 Level 3: Advanced Python
**⬜ 1.12 Iterators, Generators, Decorators, Context Managers**
Iterable vs iterator, `iter`/`next`, the iterator protocol · `yield`, generator functions, `yield from` · **generator pipelines for huge files** (streaming ETL in pure Python) · `itertools` (chain, islice, groupby, batched, product, accumulate) · decorators: writing them, with arguments, `functools.wraps` · real decorators: timing, retry, logging, caching (`lru_cache`) · `functools.partial` · context managers with classes and `contextlib`

**⬜ 1.13 Dates & Times**
`datetime`, `date`, `time`, `timedelta` · parsing & formatting (`strptime`/`strftime`, ISO 8601) · **time zones** (`zoneinfo`, UTC everywhere, naive vs aware) · Unix epoch timestamps · date arithmetic (age, durations, start of month/week) · common data-pipeline date bugs

**⬜ 1.14 Working with APIs**
HTTP refresher in Python terms · `requests`: GET/POST, params, headers, JSON, timeouts · authentication (API keys, bearer tokens, OAuth overview) · **pagination** (page/offset/cursor) · rate limits & **retries with backoff** · `httpx` & async intro · saving API data safely (idempotent)

**⬜ 1.15 Databases from Python**
DB-API concept · `sqlite3` · **PostgreSQL with `psycopg`** (connect to our Docker DB) · parameterized queries & **SQL injection** · transactions, commit/rollback · bulk inserts (`executemany`, `COPY`) · upserts (`ON CONFLICT`) · SQLAlchemy Core & ORM basics · connection pooling · pandas ⇄ SQL preview

**⬜ 1.16 Type Hints & Code Quality**
`typing`: `list[int]`, `dict[str, Any]`, `Optional`/`X | None`, `Union`, `Callable`, `TypedDict`, `Literal`, generics · `mypy` · **Pydantic** data validation (used everywhere in data engineering) · `ruff` linting & formatting · PEP 8 · writing clean, readable pipeline code

**⬜ 1.17 Testing with pytest**
Why test data code · `assert`, test discovery · fixtures, `tmp_path` · `parametrize` · testing exceptions · mocking APIs & databases (`unittest.mock`, `monkeypatch`) · coverage · testing data transformations

**⬜ 1.18 Performance & Concurrency**
Big-O for lists/dicts/sets · profiling: `timeit`, `cProfile` · memory (`sys.getsizeof`, `__slots__`, generators) · **the GIL** explained simply · `threading` vs `multiprocessing` vs `asyncio`: when to use which · `concurrent.futures` (parallel API calls, parallel file processing) · `asyncio` + `async/await` (vs JS promises/event loop)

**⬜ 1.19 Building Data APIs with FastAPI** (Express.js → FastAPI)
Why FastAPI (async, type-hint driven, auto docs) · Express ⇄ FastAPI side-by-side · `uvicorn` server, hot reload · path & query parameters with validation · request/response models with **Pydantic** · status codes & `HTTPException` · routers (like `express.Router`) & project structure · **dependency injection** (`Depends`) for DB sessions, config, auth · async vs sync endpoints (when each is right) · connecting to PostgreSQL (SQLAlchemy) · pagination, filtering & sorting endpoints for data · background tasks · middleware & CORS · authentication (API key, JWT/OAuth2 password flow) · settings with `pydantic-settings` & `.env` · file upload/download (CSV export) · streaming responses for big datasets · WebSockets (live data, used in the capstone) · testing with `TestClient` + pytest · auto-generated Swagger/OpenAPI docs · Dockerizing a FastAPI app · serving an ML model / analytics endpoint

### 🎯 Level 4: Interview & Project
**⬜ 1.20 Python Interview Mastery**
40+ "tricky Python" questions (gotchas, internals, memory model, mutability, GIL…) · 50 coding problems used in data interviews: strings, arrays, hash maps, two pointers, sliding window, sorting, stacks/queues, basic recursion · reading & processing log/CSV/JSON data · timed mock round

**⬜ Project P1: API → Postgres ETL pipeline + FastAPI data service** (`projects/p1-api-etl/`)
Real public API → pagination + retries → validation (Pydantic) → clean & transform → write CSV/JSON + load into Postgres (idempotent upsert) → logging, config via `.env`, CLI with argparse → **FastAPI service exposing the cleaned data** (filtering, pagination, stats endpoints, CSV export, Swagger docs) → pytest tests, Docker Compose, README. **Your first portfolio project.**

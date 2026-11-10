# Lesson 1.1: Exercises (step by step)

> Time needed: ~3 hours. Do the parts **in order**. Don't skip the typing; it builds muscle memory.
> Every time you open a new terminal: `cd /Users/ankitapawar/prasad/data-workspace && source .venv/bin/activate`

---

## PART A: Play in the REPL (20 min)

### Step 1: Open the Python REPL
In the VS Code terminal:
```bash
python
```
✅ You should see `>>>`, which means Python is waiting for you.

### Step 2: Try these one by one (guess the answer BEFORE pressing Enter)
```python
7 / 2
7 // 2
-7 // 2
2 ** 10
0.1 + 0.2
round(2.5)
"data" * 3
"DATA_ENG"[::-1]
len("prasad")
"5" + 5
bool([])
True + True
```
Each time your guess was wrong, re-read that section in `notes.md`. That's exactly where the learning happens.

### Step 3: Exit
```python
exit()
```

---

## PART B: Type the examples (60–90 min)

### Step 4: Create your playground file
In VS Code create `01-python/01-basics/playground.py`.

### Step 5: Type examples section by section
For each section of `notes.md` (2 → 9):
1. Type the examples into `playground.py` (add `print(...)` around expressions so you see results).
2. Add a comment header for each section, like `# ===== 4. Numbers =====`.
3. Run it:
```bash
python 01-python/01-basics/playground.py
```
4. **Change values and break things on purpose** (e.g. `int("abc")`) to see real error messages. Reading errors is a core skill.

💡 Tip: you can also run the current file with the ▶ button at the top right of VS Code.

✅ Done when you've typed and run examples from every section.

---

## PART C: Predict-the-output quiz (20 min)
Create `01-python/01-basics/quiz_answers.md`. **Write your prediction for each line first**, then run it to check, and mark ✅ or ❌.

```python
1.  print(10 / 5)
2.  print(-9 // 4, -9 % 4)
3.  print(round(3.5), round(4.5))
4.  print("Python"[1:4])
5.  print("Python"[-2:])
6.  print("a,b,,c".split(","))
7.  print("  hello   world ".split())
8.  print("-".join("abc"))
9.  print(0 or "default", "" or 0 or None)
10. print(5 and 0, "x" and "y")
11. print(bool("False"), bool(0.0), bool(" "))
12. print(int(-2.9), int("  7 "))
13. print(f"{1234.5:,.2f} | {0.075:.1%} | {7:03d}")
14. print("Zebra" < "apple")
15. print(sum([True, True, False]) * 10)
16. print(type(3 / 1), type(3 // 1))
17. x = "data"; x.upper(); print(x)
18. print(1 < 3 < 2)
```
Then answer in your own words, in the same file:
- **Q19.** Why does `"5" + 5` fail in Python but work in JavaScript?
- **Q20.** When would `value or "N/A"` give a WRONG result? Give an example.
- **Q21.** Why should money not be stored as `float`? What do you use instead?

---

## PART D: Coding exercises with an auto-checker (60 min)

### Step 6: Open the exercises file
Open `01-python/01-basics/exercises.py`. It contains **13 functions**. Each has:
- a docstring explaining what to do, plus examples
- `pass  # TODO`, which you replace with your code

> 💡 `def` creates a function, like `function` in JS. `return` sends back the result. (Functions are covered in depth in Lesson 1.6; for now just write the body.)
> Example of a finished function:
> ```python
> def double(n):
>     return n * 2
> ```

### Step 7: Run the checker
```bash
python 01-python/01-basics/check.py
```
✅ You should see a list with ❌ for every function at first (they all return `None`).

### Step 8: Solve them one by one
1. Write the code for ONE function.
2. Re-run the checker. You can check just one function:
   ```bash
   python 01-python/01-basics/check.py mask_email
   ```
3. Read the ❌ messages: they show your input, the expected output, and what you returned.
4. Repeat until all **13 show ✅**.

🧠 Rules:
- Use only what's in Lesson 1.1 (no loops or `if` needed!). Every function can be solved in 1–3 lines.
- Stuck for more than 10 minutes? Re-read the hint in the docstring, then ask me for a **hint** (not the answer).

---

## PART E: Mini challenge, receipt printer (30 min)
Create `01-python/01-basics/receipt.py` that prints this receipt **exactly** (aligned columns), using f-string format specs (no loops yet: one `print` per line is fine):

```
==========================================
                DATA STORE
==========================================
Product         Qty      Price       Total
------------------------------------------
Laptop            2  55,000.00  110,000.00
Mouse            10     500.00    5,000.00
Monitor           3  12,000.00   36,000.00
------------------------------------------
Subtotal                        151,000.00
GST (18%)                        27,180.00
Grand Total                     178,180.00
==========================================
```
Requirements:
- Store products, prices and quantities in **variables**, and **calculate** totals, GST and grand total (no hard-coded results!).
- Use `GST_RATE = 0.18` as a constant.
- The title is centered in 42 characters (`f"{'DATA STORE':^42}"`), and the lines are `"=" * 42`.
- Hint: `f"{'Laptop':<15}{2:>4}{55000:>11,.2f}{110000:>12,.2f}"`

Run it with `python 01-python/01-basics/receipt.py` and compare it character by character.

---

## PART F: Review & commit
1. Type **`review`** in the chat. I'll check `playground.py`, `quiz_answers.md`, `exercises.py` and `receipt.py`.
2. After the review, commit:
```bash
git add .
git commit -m "lesson(01-python): 1.1 basics complete"
git push
```

---

## 🆘 Troubleshooting
| Problem | Fix |
|---|---|
| `python: command not found` or wrong version | Activate the venv: `source .venv/bin/activate` |
| `IndentationError` | Use exactly 4 spaces inside a function; don't mix tabs and spaces |
| `SyntaxError` with f-strings | Check matching quotes: `f"{'Laptop':<15}"` uses single quotes inside double |
| Checker says `ModuleNotFoundError: exercises` | Run the checker from the repo root with the full path shown above |
| Everything ❌ with "got None" | You still have `pass` instead of a `return ...` line |

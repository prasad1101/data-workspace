# Lesson 1.1: Python Basics: Variables, Numbers, Strings, Booleans

> **How to study this file:** read one section, then **type** every example into `playground.py` (or the Python REPL) and run it.
> Change the values and see what happens. Typing is how your fingers learn the language.
>
> 🟢 = basic · 🟡 = intermediate · 🔴 = advanced / interview level

---

## 1. 🟢 How Python runs your code

| | JavaScript (Node) | Python |
|---|---|---|
| Run a file | `node app.js` | `python app.py` |
| Interactive shell (REPL) | `node` | `python` |
| Exit the REPL | `.exit` or Ctrl+C twice | `exit()` or Ctrl+D |
| Package manager | npm | pip / uv |
| File extension | `.js` | `.py` |

**What happens when you run `python app.py`** 🔴
1. Python reads your source code.
2. It **compiles** it into **bytecode** (a lower-level set of instructions). Imported modules get cached as `.pyc` files in `__pycache__/`.
3. The **Python Virtual Machine (PVM)** executes the bytecode line by line.

So Python is "compiled to bytecode, then interpreted". The standard implementation is called **CPython** (written in C).
> 🎯 Interview: *"Is Python compiled or interpreted?"* → "Both, in a way: CPython compiles source to bytecode, which is then interpreted by the Python Virtual Machine. There's no separate compile step for you to run."

**The REPL** is your best friend for experiments:
```
$ python
>>> 2 + 3
5
>>> "data" * 3
'datadatadata'
>>> exit()
```
In the REPL you don't need `print()`: the value of each expression is shown automatically (same as Jupyter's last line).

---

## 2. 🟢 `print()` and comments

```python
print("Hello, Data!")              # Hello, Data!
print("a", "b", "c")               # a b c        ← multiple values, separated by spaces
print("a", "b", "c", sep="-")      # a-b-c        ← custom separator
print("Loading", end="...")        # no newline at the end
print("done")                      # Loading...done
print()                            # empty line
```
| JS | Python |
|---|---|
| `console.log("a", "b")` | `print("a", "b")` |
| `// comment` | `# comment` |
| `/* multi-line */` | No real block comment. Use several `#` lines, or a docstring (below) |

```python
# This is a comment. Python ignores it.

"""
Triple-quoted strings are used as docstrings: documentation for
modules, functions and classes. When not assigned to anything, they're
effectively ignored, so people sometimes use them as block comments.
"""
```

---

## 3. 🟢 Variables

```python
name = "Prasad"        # no let / const / var, just assign
age = 30
salary = 85000.50
is_learning = True
```

### 3.1 Dynamic typing
A variable is just a **label** pointing to a value. The *value* has a type, the label doesn't:
```python
x = 10        # x points to an int
x = "ten"     # now x points to a str, totally allowed
print(type(x))   # <class 'str'>
```

### 3.2 🔴 Dynamic but STRONG typing (big difference from JS)
JavaScript is **weakly** typed: it converts types silently.
Python is **strongly** typed: it refuses to mix incompatible types.
```python
"5" + 5        # ❌ TypeError: can only concatenate str (not "int") to str
               # (JS would give "55")
"5" + str(5)   # ✅ '55'
int("5") + 5   # ✅ 10
```
> 🎯 Interview: *"Python is dynamically and strongly typed."* Dynamic = types are checked at runtime and a variable can change type. Strong = no silent implicit conversions between unrelated types.

### 3.3 Naming rules & conventions
- Allowed: letters, digits, `_`; **can't start with a digit**; case-sensitive (`age` ≠ `Age`).
- Can't use keywords (`if`, `for`, `class`, `True`, `None`, `def`, `lambda`, …). See them all: `import keyword; print(keyword.kwlist)`.
- **Conventions (PEP 8, Python's style guide):**

| Kind | Python style | JS style |
|---|---|---|
| variables, functions | `snake_case` → `total_revenue` | `camelCase` → `totalRevenue` |
| constants | `UPPER_SNAKE_CASE` → `MAX_RETRIES = 3` | same |
| classes | `PascalCase` → `OrderParser` | same |
| "private" | `_leading_underscore` | `#private` / convention |

Python has **no `const`**. `UPPER_CASE` is only a promise to other developers ("don't change this").

### 3.4 Multiple assignment & swapping
```python
a, b, c = 1, 2, 3          # like JS destructuring: const [a, b, c] = [1, 2, 3]
x = y = 0                  # both point to 0
a, b = b, a                # swap in one line, no temp variable
print(a, b)                # 2 1
```

### 3.5 🔴 Variables are references (preview of a big topic)
```python
a = [1, 2, 3]
b = a            # b points to the SAME list (like JS objects/arrays)
b.append(4)
print(a)         # [1, 2, 3, 4]  ← a changed too!
print(a is b)    # True: same object in memory
print(id(a), id(b))   # same id number = same object
```
Types are either **mutable** (can change in place: `list`, `dict`, `set`) or **immutable** (can't: `int`, `float`, `str`, `bool`, `tuple`, `None`). We go deep on this in Lesson 1.3.

`del x` removes the *name* `x` (using it afterwards gives `NameError`).

---

## 4. 🟢 Numbers

### 4.1 Types
```python
count = 42            # int: whole numbers, UNLIMITED size
price = 19.99         # float: decimal numbers (64-bit, like JS number)
big = 2 ** 100        # 1267650600228229401496703205376, no overflow!
population = 1_400_000_000   # underscores for readability (ignored by Python)
print(type(count), type(price))   # <class 'int'> <class 'float'>
```
JS has one `number` type (plus `BigInt`). Python separates `int` and `float`, and `int` never overflows.

### 4.2 Arithmetic operators
| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` `-` `*` | add, subtract, multiply | `7 * 2` | `14` |
| `/` | **true division** (always float) | `7 / 2` · `6 / 3` | `3.5` · `2.0` |
| `//` | **floor division** (rounds DOWN) | `7 // 2` | `3` |
| `%` | modulo (remainder) | `7 % 2` | `1` |
| `**` | power | `2 ** 10` | `1024` |
| `-x` | negation | `-5` | `-5` |

```python
total_minutes = 135
hours = total_minutes // 60      # 2
minutes = total_minutes % 60     # 15
print(divmod(135, 60))           # (2, 15)  ← both at once
```
**`%` is everywhere in data work:** even/odd (`n % 2 == 0`), every Nth row (`i % 100 == 0`), bucketing/hashing (`user_id % 10`).

### 4.3 🔴 Floor division with negatives (classic interview trick)
`//` rounds toward **negative infinity**, not toward zero:
```python
7 // 2      #  3
-7 // 2     # -4   (not -3!) because -3.5 rounded DOWN is -4
-7 % 2      #  1   (the result of % has the sign of the divisor)
7 % -2      # -1
int(-3.9)   # -3   ← int() truncates toward ZERO (different from //)
```
Rule that always holds: `a == (a // b) * b + (a % b)`.

### 4.4 Augmented assignment (no `++`!)
```python
count = 0
count += 1     # ✅  (count++ does NOT exist in Python)
count -= 2
count *= 10
count //= 3
count **= 2
```

### 4.5 Operator precedence (highest → lowest)
`**` → `-x` (unary) → `* / // %` → `+ -` → comparisons → `not` → `and` → `or`
```python
2 + 3 * 4      # 14
(2 + 3) * 4    # 20
-2 ** 2        # -4   ← ** binds tighter than unary minus: -(2**2)
(-2) ** 2      # 4
2 ** 3 ** 2    # 512  ← ** is right-associative: 2 ** (3 ** 2)
```
When in doubt, **use parentheses**. Readability wins.

### 4.6 🔴 Float precision: why `0.1 + 0.2 != 0.3`
```python
0.1 + 0.2              # 0.30000000000000004   (same in JS!)
0.1 + 0.2 == 0.3       # False
```
Floats are stored in binary, and 0.1 can't be represented exactly in binary (just like 1/3 = 0.333… in decimal).

How to deal with it:
```python
import math
math.isclose(0.1 + 0.2, 0.3)          # True  ← compare floats this way
round(0.1 + 0.2, 2) == 0.3            # True

from decimal import Decimal           # exact decimal math: use for MONEY 💰
Decimal("0.1") + Decimal("0.2")       # Decimal('0.3')
Decimal("0.1") + Decimal("0.2") == Decimal("0.3")   # True
```
⚠️ Create Decimals from **strings**: `Decimal(0.1)` copies the float's error (`0.1000000000000000055511…`).
> 🎯 Interview: *"How do you store money?"* → "Never as float. Use `Decimal` in Python, `NUMERIC/DECIMAL` in SQL, or store integer paise/cents."

### 4.7 🔴 `round()` uses banker's rounding
```python
round(3.14159, 2)    # 3.14
round(2.5)           # 2   ← not 3!
round(3.5)           # 4
round(-2.5)          # -2
```
Python rounds `.5` to the nearest **even** number ("banker's rounding", which avoids bias when summing many rounded numbers).
Also `round(2.675, 2)` gives `2.67`, because 2.675 is actually stored as 2.67499999…
Need classic "round half up"? Use `Decimal("2.675").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)` (`from decimal import ROUND_HALF_UP`).

### 4.8 Useful built-ins & the `math` module
```python
abs(-7)                 # 7
min(3, 9, 1)            # 1
max(3, 9, 1)            # 9
sum([10, 20, 30])       # 60
pow(2, 10)              # 1024

import math
math.floor(3.7)         # 3   (down)
math.ceil(3.2)          # 4   (up), e.g. pages needed: math.ceil(101 / 20) = 6
math.trunc(-3.7)        # -3  (toward zero)
math.sqrt(16)           # 4.0
math.pi                 # 3.141592653589793
math.log10(1000)        # 3.0
```

### 4.9 🔴 Special floats: infinity & NaN (very important later in Pandas)
```python
float("inf")            # inf, bigger than any number (useful starting value for "find minimum")
float("-inf")
nan = float("nan")      # "Not a Number": represents missing/invalid numeric data
nan == nan              # False!  NaN is not equal to anything, even itself
math.isnan(nan)         # True    ← the correct way to check
```
In Pandas, missing values in number columns become `NaN`. Remember: **never test NaN with `==`**.

### 4.10 Number conversions
```python
int("42")         # 42
int(3.99)         # 3   (truncates, does NOT round)
int("3.5")        # ❌ ValueError: invalid literal for int()
int(float("3.5")) # 3   ✅ two steps
float("3.5")      # 3.5
float("1e3")      # 1000.0 (scientific notation)
int(" 42 ")       # 42  (surrounding spaces are OK)
int("1,000")      # ❌ ValueError: remove commas first: int("1,000".replace(",", ""))
int("ff", 16)     # 255 (from base 16)
bin(10), hex(255) # ('0b1010', '0xff')
```

---

## 5. 🟢 Strings (`str`)

### 5.1 Creating strings
```python
a = 'single quotes'
b = "double quotes"            # same thing; pick one and be consistent
c = "It's easy"                # mix quotes to avoid escaping
d = """Multi-line
string keeps
line breaks"""                 # like JS `template literals` without ${}
```

### 5.2 Escape characters & raw strings
```python
print("Line1\nLine2")      # \n new line
print("Col1\tCol2")        # \t tab (TSV files!)
print("She said \"hi\"")   # \" quote inside quotes
print("C:\\Users\\data")   # \\ one backslash
print(r"C:\Users\new")     # r"" RAW string: backslashes are literal (used for regex & Windows paths)
```

### 5.3 Indexing & slicing (super important)
```
 String:   D   A   T   A   _   E   N   G
 Index:    0   1   2   3   4   5   6   7
 Negative:-8  -7  -6  -5  -4  -3  -2  -1
```
```python
s = "DATA_ENG"
s[0]        # 'D'
s[-1]       # 'G'     ← negative = from the end (JS: s.at(-1))
s[0:4]      # 'DATA'  ← [start:stop], stop is EXCLUDED
s[:4]       # 'DATA'  ← start defaults to 0
s[5:]       # 'ENG'   ← stop defaults to the end
s[-3:]      # 'ENG'   ← last 3 characters
s[::2]      # 'DT_N'  ← [start:stop:step], every 2nd char
s[::-1]     # 'GNE_ATAD'  ← REVERSE a string (classic interview one-liner)
s[100]      # ❌ IndexError
s[2:100]    # 'TA_ENG' ← slicing never errors, it just stops at the end
len(s)      # 8   (JS: s.length)
```

### 5.4 🔴 Strings are immutable
```python
s = "data"
s[0] = "D"        # ❌ TypeError: 'str' object does not support item assignment
s = "D" + s[1:]   # ✅ create a NEW string: 'Data'
```
Every string method returns a **new** string. The original never changes:
```python
name = "prasad"
name.upper()      # 'PRASAD'
print(name)       # 'prasad' ← unchanged!
name = name.upper()   # reassign to keep the result
```

### 5.5 String methods you'll use daily in data cleaning
```python
raw = "   Laptop PRO 15  "

# Case
raw.upper()            # '   LAPTOP PRO 15  '
raw.lower()            # '   laptop pro 15  '
raw.title()            # '   Laptop Pro 15  '
"hello world".capitalize()   # 'Hello world'
"Hello".swapcase()     # 'hELLO'
"Straße".casefold()    # 'strasse' (aggressive lower, for comparisons)

# Whitespace cleanup (most common cleaning step!)
raw.strip()            # 'Laptop PRO 15'   both sides (JS: trim())
raw.lstrip()           # left only
raw.rstrip()           # right only
"xxdataxx".strip("x")  # 'data'  ← strip specific characters
"$1,200".lstrip("$")   # '1,200'

# Search
"data engineering".find("eng")       # 5    (-1 if not found, like JS indexOf)
"data engineering".index("eng")      # 5    (raises ValueError if not found)
"data engineering".count("e")        # 3
"eng" in "data engineering"          # True ← most Pythonic way (JS: includes)
"report.csv".startswith("report")    # True
"report.csv".endswith((".csv", ".tsv"))  # True ← accepts a tuple of options!

# Replace
"2026/11/10".replace("/", "-")       # '2026-11-10'
"a-b-c".replace("-", "", 1)          # 'ab-c'  ← only the first 1 occurrence

# Split & join (JS: split / join, but join is called ON the separator)
"Laptop,55000,2".split(",")          # ['Laptop', '55000', '2']
"  big   data  ".split()             # ['big', 'data'] ← no argument = split on ANY whitespace, ignore extras
"a,b,,c".split(",")                  # ['a', 'b', '', 'c']
"k=v=x".split("=", 1)                # ['k', 'v=x'] ← max 1 split
"line1\nline2".splitlines()          # ['line1', 'line2']
"-".join(["2026", "11", "10"])       # '2026-11-10'  (JS: ["2026","11","10"].join("-"))
"".join(["a", "b", "c"])             # 'abc'

# Checks (return True/False)
"12345".isdigit()      # True  ← useful before int()
"abc".isalpha()        # True
"abc123".isalnum()     # True
"   ".isspace()        # True
"Hello".istitle()      # True
"HELLO".isupper()      # True

# Padding & alignment
"7".zfill(3)           # '007'     ← zero padding (IDs, months)
"data".center(10, "*") # '***data***'
"data".ljust(8, ".")   # 'data....'
"data".rjust(8)        # '    data'

# Other
"data" * 3             # 'datadatadata'
"a" + "b"              # 'ab'
"Data".removeprefix("Da")      # 'ta'  (3.9+)
"file.csv".removesuffix(".csv")  # 'file'
```
**Method chaining** works like JS:
```python
"  LAPTOP pro ".strip().lower().replace(" ", "_")   # 'laptop_pro'
```

### 5.6 🟡 f-strings: formatting like a pro (JS template literals++)
```python
name, revenue = "Laptop", 1234567.891
print(f"{name} earned {revenue}")     # JS: `${name} earned ${revenue}`
print(f"{2 + 3 = }")                  # '2 + 3 = 5'
print(f"{revenue=}")                  # 'revenue=1234567.891'  ← debugging trick!
print(f"{name.upper()} has {len(name)} letters")   # any expression works
```
**Format specs** go after `:`, giving full control over the output:
```python
x = 1234567.891
f"{x:.2f}"        # '1234567.89'     2 decimals
f"{x:,}"          # '1,234,567.891'  thousands separator
f"{x:,.2f}"       # '1,234,567.89'   both ← reports & dashboards
f"{x:_.0f}"       # '1_234_568'
f"{0.256:.1%}"    # '25.6%'          percentage (multiplies by 100!)
f"{42:05d}"       # '00042'          zero-padded int
f"{'data':>10}"   # '      data'     right-align in 10 chars
f"{'data':<10}|"  # 'data      |'    left-align
f"{'data':^10}"   # '   data   '     center
f"{'data':*^10}"  # '***data***'     custom fill char
f"{x:>15,.2f}"    # '   1,234,567.89' combine: align + width + comma + decimals
f"{1500000:.2e}"  # '1.50e+06'       scientific
f"{255:x}"        # 'ff'             hex
```
Building aligned text tables (you'll do this in the mini challenge):
```python
print(f"{'Product':<10}{'Qty':>5}{'Total':>12}")
print(f"{'Laptop':<10}{2:>5}{110000:>12,.2f}")
# Product     Qty       Total
# Laptop        2  110,000.00
```
Older styles you'll see in old code (don't write them, just recognize them):
```python
"Hello %s, you are %d" % ("Prasad", 30)         # %-formatting (oldest)
"Hello {}, you are {}".format("Prasad", 30)     # .format()
```

### 5.7 🟡 Comparing strings
```python
"apple" < "banana"     # True ← compared character by character (Unicode order)
"Zebra" < "apple"      # True ← uppercase letters come BEFORE lowercase!
"a".lower() == "A".lower()   # case-insensitive comparison
ord("A"), chr(65)      # (65, 'A') ← character ⇄ Unicode code point
```

---

## 6. 🟢 Booleans and `None`

### 6.1 Booleans
```python
is_active = True       # capital T and F (JS: true/false)
is_deleted = False
```
**Comparison operators:** `==`, `!=`, `<`, `>`, `<=`, `>=`. There's **no `===`**: Python's `==` never does type coercion, so it already behaves like JS's `===`.
```python
5 == 5.0      # True  (int and float compare by value)
"5" == 5      # False (no coercion, unlike JS's ==)
```
**Chained comparisons** (Python only, very readable):
```python
age = 25
18 <= age < 60          # True   (JS: age >= 18 && age < 60)
```

### 6.2 Logical operators: words, not symbols
| JS | Python |
|---|---|
| `&&` | `and` |
| `\|\|` | `or` |
| `!` | `not` |

```python
is_active and not is_deleted     # True
```

### 6.3 `None`: Python's "no value"
`None` replaces **both** JS `null` and `undefined`.
```python
discount = None
discount is None        # True  ✅ always check None with `is`
discount == None        # works, but not Pythonic: linters will complain
```
A function that doesn't `return` anything returns `None`.

### 6.4 🔴 Truthiness (⚠️ differs from JS!)
In `if` statements and `and/or/not`, every value counts as True or False.

**Falsy values in Python:** `False`, `None`, `0`, `0.0`, `""` (empty string), `[]` (empty list), `{}` (empty dict), `set()`, `()` (empty tuple), `range(0)`.
**Everything else is truthy.**

| Value | JS | Python |
|---|---|---|
| `[]` empty array/list | **truthy** | **falsy** ⚠️ |
| `{}` empty object/dict | **truthy** | **falsy** ⚠️ |
| `"0"` | truthy | truthy |
| `NaN` | falsy | **truthy** ⚠️ |

```python
orders = []
if not orders:                  # ✅ Pythonic "is empty?" check
    print("No orders yet")      # JS would need: orders.length === 0
bool([])      # False
bool([0])     # True ← a list with one item is truthy, even if the item is falsy
bool("False") # True ← non-empty string!
```

### 6.5 🔴 `and` / `or` return one of the operands (not just True/False)
- `a or b` → returns `a` if `a` is truthy, else returns `b`.
- `a and b` → returns `a` if `a` is falsy, else returns `b`.
- Both **short-circuit**: they stop evaluating as soon as the answer is known.
```python
"" or "Anonymous"        # 'Anonymous'  ← default value pattern (JS: || )
"Prasad" or "Anonymous"  # 'Prasad'
0 or 100                 # 100   ⚠️ 0 is falsy, so a real 0 gets replaced!
None and "x"             # None
"a" and "b"              # 'b'
```
⚠️ Python has no `??` (nullish coalescing). If `0` or `""` are valid values, write `x if x is not None else default` (Lesson 1.2).

### 6.6 🔴 Booleans are integers
```python
True + True        # 2
True * 10          # 10
sum([True, False, True, True])   # 3 ← counting matches! (used a LOT in Pandas: (df.qty > 3).sum())
isinstance(True, int)            # True: bool is a subclass of int
```

### 6.7 🔴 `is` vs `==`
- `==` → **equal value**?
- `is` → **the same object in memory**? (same `id()`)
```python
a = [1, 2]
b = [1, 2]
a == b        # True  (same contents)
a is b        # False (two different list objects)
```
**Rule:** use `is` only for `None`, `True` and `False` (singletons). Use `==` for everything else.
🔴 Trap: `a = 256; b = 256; a is b` → `True`, but with `1000` it may be `False`. CPython caches small ints (-5 to 256) as an optimization. That's exactly why you must not use `is` to compare numbers or strings.

---

## 7. 🟢 Checking & converting types

```python
type(42)                  # <class 'int'>
type("hi") == str         # True
isinstance(42, int)       # True  ✅ preferred (also handles subclasses)
isinstance(3.5, (int, float))   # True ← "is it a number?" with a tuple of types

str(42)          # '42'
str(3.5)         # '3.5'
str(None)        # 'None'
bool(0)          # False
bool("hi")       # True
float(7)         # 7.0
int(True)        # 1
```
| JS | Python |
|---|---|
| `typeof x` | `type(x)` |
| `x instanceof Y` | `isinstance(x, Y)` |
| `Number("42")` / `parseInt` | `int("42")` / `float("4.2")` |
| `String(42)` | `str(42)` |
| `Boolean(x)` / `!!x` | `bool(x)` |

---

## 8. 🟢 Reading user input
```python
name = input("Your name: ")         # program pauses until Enter
age = input("Your age: ")           # ⚠️ ALWAYS returns a str!
age = int(age)                      # convert before doing math
print(f"Next year you'll be {age + 1}")
```
(Data engineers rarely use `input()`; we'll use files, APIs and command-line arguments instead. It's still good for quick practice.)

---

## 9. 🟢 Indentation = code blocks (preview of Lesson 1.2)
Python uses **indentation** (4 spaces) where JS uses `{ }`, plus a `:` at the end of the line that opens the block:
```python
price = 1200
if price > 1000:                 # JS: if (price > 1000) {
    print("Expensive")           #   4 spaces = inside the block
    print("Apply EMI option")
print("Always runs")             # back to column 0 = outside the block
```
Wrong indentation gives an `IndentationError`. VS Code inserts 4 spaces when you press Tab in `.py` files.

---

## 10. 📋 JS → Python cheat sheet (Lesson 1.1)
| Concept | JavaScript | Python |
|---|---|---|
| Variable | `let x = 5; const Y = 1` | `x = 5` · `Y = 1` (convention) |
| Print | `console.log(x)` | `print(x)` |
| Comment | `// hi` | `# hi` |
| Template string | `` `Hi ${name}` `` | `f"Hi {name}"` |
| String length | `s.length` | `len(s)` |
| Last char | `s.at(-1)` | `s[-1]` |
| Substring | `s.slice(1, 4)` | `s[1:4]` |
| Trim | `s.trim()` | `s.strip()` |
| Contains | `s.includes("x")` | `"x" in s` |
| Join | `arr.join("-")` | `"-".join(arr)` |
| Integer division | `Math.floor(7 / 2)` | `7 // 2` |
| Power | `2 ** 10` | `2 ** 10` |
| Increment | `x++` | `x += 1` |
| true / false | `true` / `false` | `True` / `False` |
| null / undefined | `null` / `undefined` | `None` |
| And / Or / Not | `&&` `\|\|` `!` | `and` `or` `not` |
| Strict equal | `===` | `==` |
| Default value | `x \|\| "d"` · `x ?? "d"` | `x or "d"` · `x if x is not None else "d"` |
| Type | `typeof x` | `type(x)` / `isinstance` |

---

## 11. ⚠️ Top gotchas from this lesson
1. `"5" + 5` → TypeError (no auto-conversion).
2. `/` always returns a float: `6 / 3` is `2.0`.
3. `-7 // 2` is `-4`, not `-3`.
4. `round(2.5)` is `2`.
5. `0.1 + 0.2 != 0.3`, so use `math.isclose` or `Decimal`.
6. Empty list/dict/string are **falsy** (in JS `[]` is truthy).
7. `x or default` also replaces `0` and `""`.
8. `nan == nan` is `False`.
9. String methods return new strings; the original never changes.
10. Use `is` only with `None`/`True`/`False`.
11. `input()` always returns a string.
12. No `++`, no `===`, no `&&`.

---

## 12. 🎯 Interview questions (try answering out loud before opening)

<details><summary>1. Is Python compiled or interpreted?</summary>
CPython compiles source code to bytecode (cached as .pyc), which the Python Virtual Machine then interprets. So: compiled to bytecode, then interpreted.
</details>

<details><summary>2. What does "dynamically and strongly typed" mean?</summary>
Dynamic: types are attached to values and checked at runtime, and a variable can be rebound to a value of another type. Strong: Python won't implicitly convert between unrelated types ("5" + 5 raises TypeError), unlike JavaScript.
</details>

<details><summary>3. Difference between / and //? What is -7 // 2?</summary>
/ is true division and always returns a float. // is floor division, rounding toward negative infinity. -7 // 2 = -4, and -7 % 2 = 1.
</details>

<details><summary>4. Why is 0.1 + 0.2 != 0.3? How do you handle money?</summary>
Binary floating point can't represent 0.1 exactly (IEEE 754). Compare floats with math.isclose. For money use Decimal (created from strings), SQL NUMERIC, or integer cents/paise.
</details>

<details><summary>5. What does round(2.5) return and why?</summary>
2. Python 3 uses round-half-to-even ("banker's rounding") to avoid a systematic upward bias when rounding many values.
</details>

<details><summary>6. Difference between `is` and `==`?</summary>
== compares values (calls __eq__). `is` compares identity (same object, same id()). Use `is` only for singletons like None. Small-int caching makes `is` look like it works for numbers sometimes, which is a trap.
</details>

<details><summary>7. Which values are falsy in Python?</summary>
False, None, 0, 0.0, 0j, empty sequences/collections ("", [], (), {}, set(), range(0)), and objects whose __bool__ returns False or __len__ returns 0.
</details>

<details><summary>8. What do `and` / `or` return?</summary>
One of their operands, not necessarily a bool. `a or b` returns a if a is truthy, else b. `a and b` returns a if a is falsy, else b. Both short-circuit.
</details>

<details><summary>9. Are strings mutable? What happens with s += "x" in a big loop?</summary>
Strings are immutable. Each += creates a new string, copying the old one, which can lead to O(n²) total work in a loop. Collect the pieces in a list and use "".join(pieces) instead.
</details>

<details><summary>10. How do you reverse a string? Check whether "Madam" is a palindrome?</summary>
s[::-1]. Palindrome: s.lower() == s.lower()[::-1].
</details>

<details><summary>11. How do you check whether a value is NaN?</summary>
math.isnan(x) (or pandas isna). Never x == float("nan"), because NaN is not equal to itself. Trick: x != x is True only for NaN.
</details>

<details><summary>12. What is True + True? Why is that useful?</summary>
2, because bool is a subclass of int. Summing booleans counts how many conditions are true, e.g. (df["qty"] > 3).sum() in Pandas.
</details>

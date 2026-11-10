"""
Lesson 1.1 exercises: replace each `pass  # TODO` with your code.
Check your work:  python 01-python/01-basics/check.py
Only use what you learned in Lesson 1.1 (no loops or if-statements needed).
"""


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit, rounded to 1 decimal place.
    Formula: F = C * 9 / 5 + 32
    celsius_to_fahrenheit(100)  -> 212.0
    celsius_to_fahrenheit(36.6) -> 97.9
    Hint: round(number, 1)
    """
    pass  # TODO


def split_bill(total, people):
    """Split a bill equally. Return each person's share rounded to 2 decimals.
    split_bill(1000, 3) -> 333.33
    split_bill(100, 4)  -> 25.0
    """
    pass  # TODO


def minutes_to_hours(minutes):
    """Convert minutes into a string like "2h 5m".
    minutes_to_hours(125) -> "2h 5m"
    minutes_to_hours(45)  -> "0h 45m"
    Hint: // and %, then an f-string.
    """
    pass  # TODO


def is_even(n):
    """Return True if n is even, else False.
    is_even(4) -> True
    is_even(7) -> False
    Hint: a comparison already gives True/False; no `if` needed.
    """
    pass  # TODO


def initials(full_name):
    """Return the initials of a two-word name, uppercase, each followed by a dot.
    Extra spaces may be present.
    initials("prasad pawar")      -> "P.P."
    initials("  ada   lovelace ") -> "A.L."
    Hint: .split() returns a list; list[0] is the first word, list[-1] is the last.
          A word's first letter is word[0].
    """
    pass  # TODO


def clean_product_name(raw):
    """Clean a messy product name: remove surrounding spaces and use Title Case.
    clean_product_name("  laptop PRO  ")   -> "Laptop Pro"
    clean_product_name("WIRELESS mouse")   -> "Wireless Mouse"
    """
    pass  # TODO


def mask_email(email):
    """Hide an email's username except its first letter, using one * per hidden letter.
    mask_email("prasad@gmail.com") -> "p*****@gmail.com"
    mask_email("ab@x.com")         -> "a*@x.com"
    mask_email("a@b.com")          -> "a@b.com"
    Hint: .index("@") gives the position of @. Use slicing and "*" * count.
    """
    pass  # TODO


def format_price(amount):
    """Format a number as rupees, with thousands separators and 2 decimals.
    format_price(1234567.891) -> "₹1,234,567.89"
    format_price(99.5)        -> "₹99.50"
    format_price(0)           -> "₹0.00"
    """
    pass  # TODO


def reverse_words(sentence):
    """Reverse the ORDER of words (not letters). Extra spaces are removed.
    reverse_words("data is fun")      -> "fun is data"
    reverse_words("  big   data  ")   -> "data big"
    Hint: .split() gives a list, slicing [::-1] works on lists too, then " ".join(...)
    """
    pass  # TODO


def is_palindrome(text):
    """Return True if text reads the same backwards, ignoring case and spaces.
    is_palindrome("Madam")             -> True
    is_palindrome("Never odd or even") -> True
    is_palindrome("Data")              -> False
    """
    pass  # TODO


def parse_order_line(line):
    """A CSV line has: product,price,qty. Return the order total (price * qty).
    Price may have decimals, and there may be spaces around values.
    parse_order_line("Laptop,55000,2")       -> 110000
    parse_order_line("Mouse, 500, 10")       -> 5000
    parse_order_line("Monitor,12000.50,3")   -> 36001.5
    Hint: line.split(","), then convert price with float() and qty with int().
    """
    pass  # TODO


def display_name(name):
    """Return the name without surrounding spaces, or "Anonymous" if nothing is left.
    display_name("  Prasad ") -> "Prasad"
    display_name("   ")       -> "Anonymous"
    display_name("")          -> "Anonymous"
    Hint: an empty string is falsy, so think about what `or` returns.
    """
    pass  # TODO


def percent(part, whole):
    """Return part/whole as a percentage string with 1 decimal.
    percent(1, 4) -> "25.0%"
    percent(2, 3) -> "66.7%"
    Hint: there's an f-string format spec for percentages.
    """
    pass  # TODO

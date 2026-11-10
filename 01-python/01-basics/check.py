"""
Auto-checker for Lesson 1.1. Don't edit this file.

Usage (from the repo root):
    python 01-python/01-basics/check.py               # check everything
    python 01-python/01-basics/check.py mask_email    # check one function
"""

import math
import sys

import exercises as ex

TESTS = {
    "celsius_to_fahrenheit": [((0,), 32.0), ((100,), 212.0), ((-40,), -40.0), ((36.6,), 97.9)],
    "split_bill": [((1000, 3), 333.33), ((100, 4), 25.0), ((250.5, 2), 125.25)],
    "minutes_to_hours": [((125,), "2h 5m"), ((60,), "1h 0m"), ((45,), "0h 45m"), ((0,), "0h 0m")],
    "is_even": [((4,), True), ((7,), False), ((0,), True), ((-2,), True)],
    "initials": [(("prasad pawar",), "P.P."), (("Ada Lovelace",), "A.L."), (("  ada   lovelace ",), "A.L.")],
    "clean_product_name": [
        (("  laptop PRO  ",), "Laptop Pro"),
        (("WIRELESS mouse",), "Wireless Mouse"),
        (("monitor",), "Monitor"),
    ],
    "mask_email": [
        (("prasad@gmail.com",), "p*****@gmail.com"),
        (("ab@x.com",), "a*@x.com"),
        (("a@b.com",), "a@b.com"),
    ],
    "format_price": [((1234567.891,), "₹1,234,567.89"), ((99.5,), "₹99.50"), ((0,), "₹0.00")],
    "reverse_words": [(("data is fun",), "fun is data"), (("hello",), "hello"), (("  big   data  ",), "data big")],
    "is_palindrome": [
        (("Madam",), True),
        (("Data",), False),
        (("Racecar",), True),
        (("Never odd or even",), True),
    ],
    "parse_order_line": [
        (("Laptop,55000,2",), 110000),
        (("Mouse, 500, 10",), 5000),
        (("Monitor,12000.50,3",), 36001.5),
    ],
    "display_name": [(("  Prasad ",), "Prasad"), (("   ",), "Anonymous"), (("",), "Anonymous")],
    "percent": [((1, 4), "25.0%"), ((2, 3), "66.7%"), ((5, 5), "100.0%")],
}


def same(got, expected):
    if isinstance(expected, bool):
        return got is expected  # must be a real True/False, not 1/0
    if isinstance(expected, (int, float)) and isinstance(got, (int, float)) and not isinstance(got, bool):
        return math.isclose(got, expected, rel_tol=1e-9, abs_tol=1e-9)
    return got == expected


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    names = [only] if only else list(TESTS)
    passed_funcs = 0

    for name in names:
        if name not in TESTS:
            print(f"Unknown function: {name}. Options: {', '.join(TESTS)}")
            return
        func = getattr(ex, name)
        failures = []
        for args, expected in TESTS[name]:
            call = f"{name}({', '.join(repr(a) for a in args)})"
            try:
                got = func(*args)
            except Exception as e:  # show the error instead of crashing
                failures.append(f"   {call} raised {type(e).__name__}: {e}")
                continue
            if not same(got, expected):
                failures.append(f"   {call}\n      expected: {expected!r}\n      got:      {got!r}")
        if failures:
            print(f"❌ {name}")
            print("\n".join(failures))
        else:
            passed_funcs += 1
            print(f"✅ {name}")

    print("-" * 40)
    print(f"Score: {passed_funcs}/{len(names)}")
    if passed_funcs == len(names) == len(TESTS):
        print("🎉 All passing! Now do the receipt challenge (Part E), then type 'review'.")


if __name__ == "__main__":
    main()

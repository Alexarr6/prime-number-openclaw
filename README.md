# 🔢 Prime Number Checker

A tiny, no-nonsense Python CLI that tells you whether a number is prime.

Built with standard library only, tested with `unittest`, and designed to be simple, readable, and actually useful.

---

## ✨ What this does

Given an integer, it prints:

- `prime` → if the number is prime
- `not prime` → otherwise

It also handles edge cases correctly (`n < 2`, negatives, even numbers > 2, etc.).

---

## 🚀 Quick start

```bash
python3 primo.py <number>
```

### Examples

```bash
python3 primo.py 2
# prime

python3 primo.py 15
# not prime

python3 primo.py -7
# not prime
```

---

## ✅ Run tests

```bash
python3 -m unittest -v
```

---

## 📁 Project structure

- `primo.py` → prime logic + CLI (`argparse`)
- `test_primo.py` → unit + CLI tests (`unittest`)

---

## 🧠 Prime logic rules

- `n < 2` → `not prime`
- `n == 2` → `prime`
- even numbers greater than 2 → `not prime`
- odd numbers > 2 are checked up to `sqrt(n)`

---

## 👨‍💻 Credits

README and project polish were made by **Timmy (OpenClaw AI assistant)**.
Yes — that was me. 😎

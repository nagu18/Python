# 🐍 Python Practice Assignments

## 1. 💸 Bill Splitter Function

**Description:**  
Write a function that takes two inputs:
- `total_bill`: the total amount of the bill
- `num_people`: number of people sharing the bill

**Goal:**  
Return how much each person should pay.

**Example:**
```python
def split_bill(total_bill, num_people):
    return total_bill / num_people

# Test
print(split_bill(1000, 4))  # Output: 250.0
```

---

## 2. 📧 Email Validator Function

**Description:**  
Create a function that checks if an email address is valid.

**Requirements:**
- Must contain `@` and `.`
- Basic format check (you can improve it later)

**Example:**
```python
def is_valid_email(email):
    return "@" in email and "." in email and email.index("@") < email.rindex(".")

# Test
print(is_valid_email("abc@gmail.com"))     # Output: True
print(is_valid_email("abcgmail.com"))      # Output: False
```

---

## 3. 🛒 Shopping Cart Total with Sales Tax

**Description:**  
Write a function that takes a list of item prices and returns the total including 10% sales tax.

**Example:**
```python
def cart_total(prices):
    total = sum(prices)
    tax = total * 0.10
    return total + tax

# Test
print(cart_total([100, 200, 300]))  # Output: 660.0
```

---

## 4. 🔁 Unit Converter (Kilometers to Miles)

**Description:**  
Write a function that converts kilometers to miles.

**Conversion Formula:**  
```
1 kilometer = 0.62137 miles
```

**Example:**
```python
def km_to_miles(km):
    return km * 0.62137

# Test
print(km_to_miles(10))  # Output: 6.2137
```

---

## 📦 Python Modules Overview

### ✅ Built-in Modules  
Available by default in Python:
- `os`
- `sys`
- `math`
- `random`
- `datetime`
- `json`

### 🛠️ User-defined Modules  
Your own `.py` files that can be imported and reused across projects.

### 🌐 Third-party (External) Modules  
Must be installed using `pip`.

**Examples:**
- `requests`
- `Django`
- `numpy`
- `flask`
- `pygame`
- `pytest`

**Installation Command:**
```bash
pip install module_name
```

---

📁 Save this file as `python_practice.md` or include it in your GitHub repository for reference.
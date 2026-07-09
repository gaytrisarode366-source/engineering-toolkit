# 🔧 Engineering Student Toolkit

A Python-based toolkit built for engineering students to solve common academic problems quickly — from unit conversions to CGPA calculations.

> Built by a student, for students. 🎓  
> Savitribai Phule Pune University

---

## ✨ Features

| Module | Description |
|--------|-------------|
| 📐 **Unit Converter** | Length, Temperature conversions |
| ⚡ **Physics Calculators** | Ohm's Law, KE, PE, Force |
| 🔢 **Math Utilities** | Quadratic roots, Prime check, GCD, LCM |
| 🎓 **CGPA Calculator** | Calculate CGPA from grade points & credits |
| 📊 **Grade Converter** | Percentage → SPPU Grade system |

---

## 🚀 Getting Started

### Requirements
- Python 3.7+
- No external libraries needed (uses only built-in `math`)

### Run the toolkit

```bash
git clone https://github.com/YOUR_USERNAME/engineering-toolkit.git
cd engineering-toolkit
python toolkit.py
```

---

## 📖 Usage Examples

### Unit Conversion
```python
from toolkit import convert_length, convert_temperature

print(convert_length(100, 'cm', 'm'))        # 1.0
print(convert_temperature(37, 'C', 'F'))     # 98.6
```

### Ohm's Law
```python
from toolkit import ohms_law

voltage = ohms_law(I=2, R=5)   # V = I × R = 10V
current = ohms_law(V=10, R=5)  # I = V / R = 2A
```

### Quadratic Equation Roots
```python
from toolkit import quadratic_roots

roots = quadratic_roots(1, -5, 6)  # x² - 5x + 6 = 0
print(roots)  # (3.0, 2.0)
```

### CGPA Calculator (SPPU Style)
```python
from toolkit import calculate_cgpa

grades = [(8, 4), (9, 3), (7, 4), (8, 3)]  # (grade_point, credits)
print(calculate_cgpa(grades))  # 8.0
```

### Percentage to Grade
```python
from toolkit import percentage_to_grade

print(percentage_to_grade(72))  # O (Outstanding)
print(percentage_to_grade(55))  # A (Very Good)
```

---

## 📁 Project Structure

```
engineering-toolkit/
│
├── toolkit.py        # Main toolkit with all functions
├── README.md         # Project documentation
└── requirements.txt  # Dependencies (none required)
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add more engineering calculators
- Improve existing functions
- Add unit tests

```bash
# Fork → Clone → Make changes → Pull Request
```

---

## 📜 License

MIT License — free to use and modify.

---

## 👩‍💻 Author

**Gaytri Sarode**  
---



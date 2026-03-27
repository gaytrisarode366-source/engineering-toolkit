"""
Engineering Student Toolkit
============================
A collection of useful calculators and utilities for engineering students.
Author: Gaytri Sarode
University: Savitribai Phule Pune University
"""

import math


# ─────────────────────────────────────────
# 1. UNIT CONVERTER
# ─────────────────────────────────────────

def convert_length(value, from_unit, to_unit):
    """Convert between length units."""
    to_meters = {
        "mm": 0.001, "cm": 0.01, "m": 1,
        "km": 1000, "inch": 0.0254, "ft": 0.3048
    }
    if from_unit not in to_meters or to_unit not in to_meters:
        return "Invalid unit"
    meters = value * to_meters[from_unit]
    return meters / to_meters[to_unit]


def convert_temperature(value, from_unit, to_unit):
    """Convert between Celsius, Fahrenheit, and Kelvin."""
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        return "Invalid unit"

    if to_unit == "C":
        return round(celsius, 2)
    elif to_unit == "F":
        return round((celsius * 9 / 5) + 32, 2)
    elif to_unit == "K":
        return round(celsius + 273.15, 2)
    else:
        return "Invalid unit"


# ─────────────────────────────────────────
# 2. PHYSICS CALCULATORS
# ─────────────────────────────────────────

def ohms_law(V=None, I=None, R=None):
    """Calculate V, I, or R using Ohm's Law: V = I * R"""
    if V is None and I is not None and R is not None:
        return round(I * R, 4)
    elif I is None and V is not None and R is not None:
        return round(V / R, 4)
    elif R is None and V is not None and I is not None:
        return round(V / I, 4)
    else:
        return "Provide exactly two values"


def kinetic_energy(mass_kg, velocity_ms):
    """KE = 0.5 * m * v^2"""
    return round(0.5 * mass_kg * velocity_ms ** 2, 4)


def potential_energy(mass_kg, height_m, g=9.81):
    """PE = m * g * h"""
    return round(mass_kg * g * height_m, 4)


def force(mass_kg, acceleration_ms2):
    """F = m * a (Newton's Second Law)"""
    return round(mass_kg * acceleration_ms2, 4)


# ─────────────────────────────────────────
# 3. MATHS UTILITIES
# ─────────────────────────────────────────

def quadratic_roots(a, b, c):
    """Find roots of ax^2 + bx + c = 0"""
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        r1 = (-b + math.sqrt(discriminant)) / (2 * a)
        r2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return round(r1, 4), round(r2, 4)
    elif discriminant == 0:
        r = -b / (2 * a)
        return round(r, 4), round(r, 4)
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-discriminant) / (2 * a)
        return f"{round(real,4)}+{round(imag,4)}i", f"{round(real,4)}-{round(imag,4)}i"


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n):
    """Return factorial of n."""
    return math.factorial(n)


def gcd(a, b):
    """Return GCD of two numbers."""
    return math.gcd(a, b)


def lcm(a, b):
    """Return LCM of two numbers."""
    return abs(a * b) // math.gcd(a, b)


# ─────────────────────────────────────────
# 4. CGPA CALCULATOR
# ─────────────────────────────────────────

def calculate_cgpa(grades: list):
    """
    Calculate CGPA from a list of (grade_points, credits) tuples.
    Example: [(8, 4), (9, 3), (7, 4)]
    """
    total_points = sum(g * c for g, c in grades)
    total_credits = sum(c for _, c in grades)
    if total_credits == 0:
        return 0
    return round(total_points / total_credits, 2)


def percentage_to_grade(percentage):
    """Convert percentage to grade (SPPU style)."""
    if percentage >= 75:
        return "O (Outstanding)"
    elif percentage >= 65:
        return "A+ (Excellent)"
    elif percentage >= 55:
        return "A (Very Good)"
    elif percentage >= 50:
        return "B+ (Good)"
    elif percentage >= 45:
        return "B (Above Average)"
    elif percentage >= 40:
        return "C (Average / Pass)"
    else:
        return "F (Fail)"


# ─────────────────────────────────────────
# 5. DEMO / MAIN
# ─────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("  🔧 Engineering Student Toolkit")
    print("  Savitribai Phule Pune University")
    print("=" * 50)

    print("\n📐 Unit Conversion:")
    print(f"  100 cm = {convert_length(100, 'cm', 'm')} m")
    print(f"  37°C = {convert_temperature(37, 'C', 'F')}°F")

    print("\n⚡ Ohm's Law (V=?, I=2A, R=5Ω):")
    print(f"  Voltage = {ohms_law(I=2, R=5)} V")

    print("\n🔢 Quadratic Roots (x² - 5x + 6 = 0):")
    print(f"  Roots = {quadratic_roots(1, -5, 6)}")

    print("\n🎓 CGPA Calculator:")
    grades = [(8, 4), (9, 3), (7, 4), (8, 3)]
    print(f"  Grades: {grades}")
    print(f"  CGPA = {calculate_cgpa(grades)}")

    print("\n📊 Grade Check:")
    print(f"  72% = {percentage_to_grade(72)}")
    print(f"  85% = {percentage_to_grade(85)}")

    print("\n✅ All functions working!")

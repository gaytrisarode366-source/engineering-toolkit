import math

# ==========================
# UNIT CONVERTER
# ==========================

length_units = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "inch": 0.0254,
    "ft": 0.3048
}


def convert_length(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in length_units or to_unit not in length_units:
        raise ValueError("Invalid unit.")

    meters = value * length_units[from_unit]
    return meters / length_units[to_unit]


def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit == to_unit:
        return value

    # Convert to Celsius
    if from_unit == "F":
        c = (value - 32) * 5 / 9
    elif from_unit == "K":
        c = value - 273.15
    else:
        c = value

    # Convert Celsius to target
    if to_unit == "F":
        return c * 9 / 5 + 32
    elif to_unit == "K":
        return c + 273.15
    else:
        return c


# ==========================
# PHYSICS
# ==========================

def ohms_law(V=None, I=None, R=None):

    if V is None:
        return I * R

    if I is None:
        return V / R

    if R is None:
        return V / I

    return "Provide only two values."


def force(mass, acceleration):
    return mass * acceleration


def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2


def potential_energy(mass, gravity, height):
    return mass * gravity * height


# ==========================
# MATH UTILITIES
# ==========================

def quadratic_roots(a, b, c):

    d = b ** 2 - 4 * a * c

    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2 * a)
        r2 = (-b - math.sqrt(d)) / (2 * a)
        return (r1, r2)

    elif d == 0:
        r = -b / (2 * a)
        return (r,)

    else:
        real = -b / (2 * a)
        imag = math.sqrt(-d) / (2 * a)
        return (complex(real, imag), complex(real, -imag))


def prime_check(n):

    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def gcd(a, b):
    return math.gcd(a, b)


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


# ==========================
# CGPA
# ==========================

def calculate_cgpa(subjects):

    total_points = 0
    total_credits = 0

    for grade, credit in subjects:
        total_points += grade * credit
        total_credits += credit

    if total_credits == 0:
        return 0

    return round(total_points / total_credits, 2)


# ==========================
# PERCENTAGE TO GRADE
# (SPPU Style Example)
# ==========================

def percentage_to_grade(percent):

    if percent >= 90:
        return "O"

    elif percent >= 80:
        return "A+"

    elif percent >= 70:
        return "A"

    elif percent >= 60:
        return "B+"

    elif percent >= 55:
        return "B"

    elif percent >= 50:
        return "C"

    elif percent >= 45:
        return "P"

    else:
        return "F"


# ==========================
# MENU
# ==========================

def menu():

    while True:

        print("\n====== ENGINEERING TOOLKIT ======")
        print("1. Length Converter")
        print("2. Temperature Converter")
        print("3. Ohm's Law")
        print("4. Force")
        print("5. Kinetic Energy")
        print("6. Potential Energy")
        print("7. Quadratic Roots")
        print("8. Prime Check")
        print("9. GCD")
        print("10. LCM")
        print("11. CGPA Calculator")
        print("12. Percentage to Grade")
        print("0. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            v = float(input("Value: "))
            f = input("From Unit: ")
            t = input("To Unit: ")
            print("Answer:", convert_length(v, f, t))

        elif choice == "2":
            v = float(input("Temperature: "))
            f = input("From (C/F/K): ")
            t = input("To (C/F/K): ")
            print("Answer:", round(convert_temperature(v, f, t), 2))

        elif choice == "3":
            print("Leave unknown blank")

            V = input("Voltage: ")
            I = input("Current: ")
            R = input("Resistance: ")

            V = float(V) if V else None
            I = float(I) if I else None
            R = float(R) if R else None

            print("Answer:", ohms_law(V, I, R))

        elif choice == "4":
            m = float(input("Mass: "))
            a = float(input("Acceleration: "))
            print("Force =", force(m, a))

        elif choice == "5":
            m = float(input("Mass: "))
            v = float(input("Velocity: "))
            print("KE =", kinetic_energy(m, v))

        elif choice == "6":
            m = float(input("Mass: "))
            g = float(input("Gravity: "))
            h = float(input("Height: "))
            print("PE =", potential_energy(m, g, h))

        elif choice == "7":
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            print(quadratic_roots(a, b, c))

        elif choice == "8":
            n = int(input("Number: "))
            print(prime_check(n))

        elif choice == "9":
            a = int(input("First Number: "))
            b = int(input("Second Number: "))
            print(gcd(a, b))

        elif choice == "10":
            a = int(input("First Number: "))
            b = int(input("Second Number: "))
            print(lcm(a, b))

        elif choice == "11":

            n = int(input("Number of subjects: "))

            subjects = []

            for i in range(n):
                gp = float(input(f"Subject {i+1} Grade Point: "))
                cr = float(input(f"Subject {i+1} Credits: "))
                subjects.append((gp, cr))

            print("CGPA =", calculate_cgpa(subjects))

        elif choice == "12":
            p = float(input("Percentage: "))
            print("Grade:", percentage_to_grade(p))

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu()

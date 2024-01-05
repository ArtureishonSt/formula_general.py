import math

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No hay soluciones reales"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"La única solución es x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Las soluciones son x1 = {x1} y x2 = {x2}"


print(quadratic_formula(16, 80,4))


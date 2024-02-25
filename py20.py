import math

def ln_one_plus_x(x, tol):
    result = 0
    term = x
    n = 1
    while abs(term) > tol:
        result += term
        n += 1
        term = (-1)**(n-1) * (x**n) / n
    return round(result, 8)

x = 0.1
tol = 1e-06
result = ln_one_plus_x(x, tol)
print(result)
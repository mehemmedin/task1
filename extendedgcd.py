def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0   # gcd, x, y
    
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y


# test
a = 30
b = 20

g, x, y = extended_gcd(a, b)

print("gcd:", g)
print("x:", x)
print("y:", y)
print(f"form: {a}*{x} + {b}*{y} = {a*x + b*y}")

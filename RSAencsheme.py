

import random
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(start=100, end=300):
    while True:
        p = random.randint(start, end)
        if is_prime(p):
            return p

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(e, phi):
    g, x, _ = egcd(e, phi)
    if g != 1:
        raise Exception("No modular inverse")
    return x % phi


def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    if math.gcd(e, phi) != 1:
        e = 3
        while math.gcd(e, phi) != 1:
            e += 2
    d = modinv(e, phi)
    return (e, n), (d, n)  


def encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

def decrypt(ciphertext, private_key):
    d, n = private_key
    return "".join(chr(pow(c, d, n)) for c in ciphertext)


public_key, private_key = generate_keys()

msg = "MURADIN QIZLARLA HEMISE PROBLEMI OLUR"
cipher = encrypt(msg, public_key)
plain = decrypt(cipher, private_key)

print("Public key:", public_key)
print("Ciphertext:", cipher)
print("Decrypted:", plain)
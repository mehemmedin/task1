import random

#Public parameters 
p = 23        # large prime
g = 5         # primitive root modulo p


#Alice
a = random.randint(1, p-2) #private key
A = pow(g, a, p)   #public key

#Bob
b = random.randint(1, p-2) #private key
B = pow(g, b, p)   #public key


# Shared secret computation
alice_shared = pow(B, a, p)
bob_shared   = pow(A, b, p)

print("Public prime (p):", p)
print("Generator (g):", g)
print("Alice public key (A):", A)
print("Bob public key (B):", B)
print("Alice shared key:", alice_shared)
print("Bob shared key:", bob_shared)
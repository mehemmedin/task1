import random

# Public parameters
p = 23
g = 5
seed = random.randint(1, p - 2)  # secret seed

def dl_prg(seed, length):
    x = seed
    bits = []
    for _ in range(length):
        x = pow(g, x, p)      # x_{i+1} = g^{x_i} mod p
        bits.append(x % 2)    # output 1 bit (LSB)
    return bits


output_bits = dl_prg(seed, 20)

print("Seed:", seed)
print("PRG output bits:", output_bits)
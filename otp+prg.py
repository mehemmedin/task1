import random


def prg(seed, length):
    random.seed(seed)  
    return ''.join(str(random.randint(0, 1)) for _ in range(length))


def to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def to_text(binary):
    res = ""
    for i in range(0, len(binary), 8):
        res += chr(int(binary[i:i+8], 2))
    return res


def xor(a, b):
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

msg = "Salam"
binary_msg = to_binary(msg)

seed = 12345 
key = prg(seed, len(binary_msg)) 

cipher = xor(binary_msg, key)
decrypted = xor(cipher, key)

print("Message   :", msg)
print("Binary    :", binary_msg)
print("Key (PRG) :", key)
print("Cipher    :", cipher)
print("Decrypted :", to_text(decrypted))
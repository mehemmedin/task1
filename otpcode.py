import random


def to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)


def to_text(binary):
    result = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        result += chr(int(byte, 2))
    return result


def generate_key(n):
    return ''.join(str(random.randint(0, 1)) for _ in range(n))


def xor(a, b):
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))



msg = "Salam"
binary_msg = to_binary(msg)

key = generate_key(len(binary_msg))

cipher = xor(binary_msg, key)
decrypted = xor(cipher, key)

print("Message:", msg)
print("Binary :", binary_msg)
print("Key    :", key)
print("Cipher :", cipher)
print("Decrypted:", to_text(decrypted))
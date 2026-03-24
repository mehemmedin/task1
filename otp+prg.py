import random

def prg(seed, length):
    random.seed(seed)
    return ''.join(str(random.randint(0, 1)) for _ in range(length))

def to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)


def from_binary(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)


def otp_xor(data_bits, key_bits):
    return ''.join(
        str(int(b) ^ int(k)) for b, k in zip(data_bits, key_bits)
    )

def otp_prg_encrypt(message, seed):
    msg_bits = to_binary(message)
    key = prg(seed, len(msg_bits))
    cipher_bits = otp_xor(msg_bits, key)
    return cipher_bits

def otp_prg_decrypt(cipher_bits, seed):
    key = prg(seed, len(cipher_bits))
    msg_bits = otp_xor(cipher_bits, key)
    return from_binary(msg_bits)


seed = 12345
message = "HELLO"

cipher = otp_prg_encrypt(message, seed)
plain = otp_prg_decrypt(cipher, seed)

print("Cipher bits:", cipher)
print("Decrypted:", plain)
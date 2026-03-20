from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def prf(key, r, length):
    cipher = AES.new(key, AES.MODE_ECB)
    out = b""
    counter = 0

    while len(out) < length:
        block = r + counter.to_bytes(4, 'big')  # 12 + 4 = 16
        out += cipher.encrypt(block)
        counter += 1

    return out[:length]

def encrypt(key, message):
    m = message.encode()
    r = get_random_bytes(12)        # random nonce (randomization)
    keystream = prf(key, r, len(m))
    c = bytes(x ^ y for x, y in zip(m, keystream))
    return r, c

def decrypt(key, r, c):
    keystream = prf(key, r, len(c))
    m = bytes(x ^ y for x, y in zip(c, keystream))
    return m.decode()
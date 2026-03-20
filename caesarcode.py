def encrypt(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            result += chr((ord(c.lower()) - 97 + shift) % 26 + 97)
        else:
            result += c
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

msg = "murad hemise qizlardan uzaq gezir"
s = 3

enc = encrypt(msg, s)
dec = decrypt(enc, s)

print(enc)
print(dec)
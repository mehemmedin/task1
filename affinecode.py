def encrypt(text, a, b):
    result = ""
    for c in text:
        if c.isalpha():
            x = ord(c.lower()) - 97
            result += chr((a * x + b) % 26 + 97)
        else:
            result += c
    return result



def mod_inverse(a):
    for i in range(26):
        if (a * i) % 26 == 1:
            return i


def decrypt(text, a, b):
    result = ""
    a_inv = mod_inverse(a)
    
    for c in text:
        if c.isalpha():
            y = ord(c.lower()) - 97
            result += chr((a_inv * (y - b)) % 26 + 97)
        else:
            result += c
    return result



msg = "qizlar muradla biryerde gezmek istemirler"
a = 5   
b = 8

enc = encrypt(msg, a, b)
dec = decrypt(enc, a, b)

print(enc)
print(dec)
from collections import Counter
import string

ciphertext = "xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadds"

alphabet = string.ascii_lowercase


def caesarDecrypt(text, shift):
    result = ""
    for ch in text:
        if ch in alphabet:
            new_index = (alphabet.index(ch) - shift) % 26
            result += alphabet[new_index]
        else:
            result += ch
    return result


def showFrequencies(text):
    freq = Counter(text)
    print("Letter frequencies:")
    for letter, count in freq.most_common():
        print(f"{letter} : {count}")


def bruteForceCaesar(text):
    print("\nAll possible decryptions:\n")
    for shift in range(26):
        decrypted = caesarDecrypt(text, shift)
        print(f"Shift {shift:2}: {decrypted}")

showFrequencies(ciphertext)
bruteForceCaesar(ciphertext)
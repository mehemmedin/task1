# task1
It enters a while loop that runs until both numbers become equal.
Inside the loop:
If n1 > n2, it subtracts n2 from n1.
Otherwise, it subtracts n1 from n2.
This repeated subtraction is based on the idea that:
Subtracting the smaller number from the larger does not change the GCD.
Eventually, both numbers reduce to the same value.
When n1 == n2, the loop stops.
That final value is the Greatest Common Divisor (GCD).

# task2
Caesar (Shift) Cipher:

In this method, the text is processed letter by letter. If a character is a letter, it is first converted to lowercase. The operation ord(c.lower()) - 97 turns the letter into a number from 0 to 25 (a=0, b=1, …, z=25). Then the shift value is added, and % 26 is applied so that after z it wraps back to a. Finally, chr() converts the number back to a letter. The decrypt function does the same operation but with a negative shift, moving the letters backward.

Affine Cipher:

This method is slightly more complex than Caesar. Each letter is transformed using two parameters: a and b. First, the letter is converted to 0–25 using ord(c.lower()) - 97. Then the formula (a * x + b) % 26 is applied. Here, a scrambles the letter, and b adds a shift. The value of a must be coprime with 26, or decryption won’t work. To decrypt, the modular inverse of a is found using mod_inverse(a). Then the decryption formula a_inv * (y - b) % 26 is applied. This operation perfectly restores the original text.

# task3
Convert the message to binary (to_binary).
Generate a random binary key of the same length (generate_key).
XOR the binary message with the key to get the cipher (xor).
To decrypt, XOR the cipher with the same key to recover the original message (xor again).

Each bit of the message is combined with a random key bit.
Security is perfect if the key is truly random, as long as the key is never reused.
to_text converts the binary back to readable characters.

# task4
Convert the message to binary (to_binary).
Generate a pseudorandom binary key of the same length using a PRG seeded with a number (prg(seed, length)).
XOR the message bits with the key bits to produce the cipher (otp_xor).
To decrypt, regenerate the same key using the same seed and XOR again to recover the original message (otp_prg_decrypt).

The PRG allows using a shorter, repeatable seed instead of a full random key.
Security is weaker than true OTP because the PRG is deterministic.
XOR is symmetric, so the same operation encrypts and decrypts.

# task5
caesarDecrypt – shifts each letter backward by a given shift value to attempt decryption. Non-letter characters stay the same.
showFrequencies – counts how often each letter appears in the ciphertext using Counter and prints them in order of frequency.
bruteForceCaesar – tries all 26 possible shifts, printing each potential decryption. This is useful when the key (shift) is unknown.

Frequency analysis helps guess the correct shift by comparing common letters (like 'e', 't') in English.
Brute-force ensures you see every possible outcome if the shift is small or unknown.
Works only for simple Caesar/shift ciphers; won’t break more complex ciphers like Affine or OTP.

# task6
Padding (pad) – ensures data blocks are 16 bytes for AES, since AES works on 16-byte blocks.
Pseudo-Random Function (prf) – generates a keystream of a given length using AES in ECB mode.
Takes a key key, a random nonce r, and desired output length.
Concatenates r with a 4-byte counter and encrypts each block.
Produces a continuous keystream for XORing with the message.
Encryption (encrypt) –
Converts the message to bytes.
Generates a random 12-byte nonce r.
Generates the keystream via prf.
XORs each byte of the message with the keystream to get the cipher.
Decryption (decrypt) –
Regenerates the same keystream using the key and nonce.
XORs the cipher with the keystream to recover the original message.

Security relies on a truly random key and nonce.
This is essentially AES as a stream cipher, similar in principle to OTP but using AES to generate the keystream.
XOR is symmetric: the same operation encrypts and decrypts.

# task7
Padding (pad) – ensures data blocks are 16 bytes for AES, since AES works on 16-byte blocks.
Pseudo-Random Function (prf) – generates a keystream of a given length using AES in ECB mode.
Takes a key key, a random nonce r, and desired output length.
Concatenates r with a 4-byte counter and encrypts each block.
Produces a continuous keystream for XORing with the message.
Encryption (encrypt) –
Converts the message to bytes.
Generates a random 12-byte nonce r.
Generates the keystream via prf.
XORs each byte of the message with the keystream to get the cipher.
Decryption (decrypt) –
Regenerates the same keystream using the key and nonce.
XORs the cipher with the keystream to recover the original message.

Security relies on a truly random key and nonce.
This is essentially AES as a stream cipher, similar in principle to OTP but using AES to generate the keystream.
XOR is symmetric: the same operation encrypts and decrypts.

# task8
Prime generation (is_prime, generate_prime) – randomly picks primes p and q to create the RSA modulus n = p * q.
Key generation (generate_keys) –
Computes phi = (p-1)*(q-1).
Chooses a public exponent e (commonly 65537) that is coprime with phi.
Computes private exponent d as the modular inverse of e modulo phi.
Returns public key (e, n) and private key (d, n).

Encryption (encrypt) – for each character m in the message, compute:

c = m^e mod n

Produces a list of integers as the ciphertext.

Decryption (decrypt) – for each integer c in the ciphertext, compute:

m = c^d mod n

Converts it back to characters to recover the original message.

Security relies on the difficulty of factoring large n.
Only works reliably for small messages or with padding schemes in practice.
This is a textbook RSA implementation: simple but demonstrates public/private key cryptography.

# task9
Public parameters – a large prime p and a generator g (primitive root modulo p) are chosen and shared publicly.
Private keys –
Alice selects a secret a.
Bob selects a secret b.
Public keys –
Alice computes A = g^a mod p.
Bob computes B = g^b mod p.
These are exchanged over the insecure channel.

Shared secret – both compute the shared key using the other’s public key:

Alice: shared = B^a mod p
Bob:   shared = A^b mod p
Due to modular exponentiation properties, alice_shared == bob_shared.

Key points:

The shared key can be used for symmetric encryption afterward.
An eavesdropper knowing p, g, A, B cannot easily compute the shared key without solving the discrete logarithm problem.

# task10
Public parameters – a prime p and a generator g (primitive root modulo p).
Seed – a secret initial value used as the PRG’s internal state.
PRG function (dl_prg) – generates pseudorandom bits using the discrete logarithm principle:
For each step, update x with x = g^x mod p.
Output the least significant bit (x % 2) as the pseudorandom bit.
Repeat to generate the desired number of bits.
Security idea – predicting future bits without knowing the seed is hard because it would require solving the discrete logarithm problem modulo p.

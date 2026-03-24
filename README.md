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


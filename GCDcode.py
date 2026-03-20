n1=int(input('Enter the first number: '))
n2=int(input('Enter the second number: '))

while n1!=n2:
    if n1>n2:
        n1=n1-n2
    else:
        n2=n2-n1
print(f'GCD of 2 given numbers is {n1}')
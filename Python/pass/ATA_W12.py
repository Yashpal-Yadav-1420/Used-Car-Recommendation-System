"""a = 233
print(bin(a)[2:])"""

"""x = int(input("Enter your number: "))
for i in range(x-2):
    a = x%2
    x = int(x/2) 
    print(a)"""

# decimal to binary 
"""def dec_to_bin(n):
    b = 0
    while(n!=0):
        r = n%2
        b=(b*10)+r
        n = int(n/2)
    return b
n = int(input("Enter your number: "))
a = dec_to_bin(n)
x = str(a)
for i in x:
    s = []
    c = s.append(i)
    s = [c]
    print(s)"""

def dec_to_bin(n):
    b = ""
    while n != 0:
        r = n % 2
        b = str(r) + b  
        n = n // 2
    return b

n = int(input("Enter your number: "))
binary_representation = dec_to_bin(n)
for digit in binary_representation:
    
    print(digit)


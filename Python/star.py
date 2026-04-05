'''n = int(input("Enter your number: "))
i = 0
while(i < n):
    print("* "*(i+1))
    i+=1'''

"""n = int(input("Enter your number: "))
s = str(n)
i =0
b =0
while (i<len(s)):
    a = n/10
    b +=a
    i+=1
print(b)"""

"""Task Completed
The code has several issues that prevent it from correctly summing the digits of the entered number:

Incorrect calculation inside the loop: a = n/10 computes the same value (n divided by 10) in every iteration, since n is not modified. This does not extract individual digits.

Loop logic error: The loop runs len(s) times (where s is the string representation of n), but it adds the same a value each time, resulting in b = len(s) * (n / 10). For example, for n=123, len(s)=3, so b = 3 * (123 / 10) = 36.9, which is not the sum of digits (1+2+3=6).

No digit extraction: To sum digits, you need to repeatedly extract the last digit using n % 10, add it to the sum, and remove it by integer division n = n // 10.

Float division: In Python 3, / performs float division, so n/10 is a float (e.g., 12.3), and summing floats may lead to imprecise results for large numbers.

The correct way to sum the digits is:


n = int(input("Enter your number: "))
b = 0
while n > 0:
    b += n % 10
    n = n // 10
print(b)
This extracts each digit, sums them, and handles the number correctly."""

n = int(input("Enter your number: "))
b = 0
while n > 0:
    b += n % 10
    n = n // 10
print(b)
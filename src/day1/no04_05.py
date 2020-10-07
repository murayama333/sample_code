number1 = 18
number2 = 12

min_number = number1
if number1 > number2:
    min_number = number2

gcd = 0
for i in range(1, min_number + 1):
    if number1 % i == 0 and number2 % i == 0:
        gcd = i
print("GCD:", gcd)
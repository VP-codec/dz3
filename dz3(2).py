first = int(input("First number: "))
second = int(input("Second number: "))
total_sum = 0
count = 0
for i in range(first, second + 1):
    total_sum += i
    count += 1
average = total_sum / count
print(f"Sum: {total_sum}")
print(f"Average: {average}")

print("---")

length = int(input("Line length: "))
symbol = input("Symbol: ")
for i in range(5):
    for j in range(length):
        print(symbol, end="")
    print()

print("---")

number = int(input("Enter number: "))
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")

print("---")

number = int(input("Enter number: "))
total_sum = 0
maximum = 0
minimum = 9
while number > 0:
    digit = number % 10
    total_sum += digit
    if digit > maximum:
        maximum = digit
    if digit < minimum:
        minimum = digit
    number //= 10
print(f"Sum: {total_sum}, Max: {maximum}, Min: {minimum}")

print("---")

number = int(input("Enter number: "))
print("Program should check if number is prime")
is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")

print("---")

number = int(input("Enter number: "))
print("Program should check if number is Fibonacci")
a, b = 0, 1
is_fibonacci = False
if number == 0 or number == 1:
    is_fibonacci = True
else:
    while b < number:
        a, b = b, a + b
    if b == number:
        is_fibonacci = True
if is_fibonacci:
    print(f"{number} is Fibonacci")
else:
    print(f"{number} is not Fibonacci")
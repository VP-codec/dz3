first = int(input("First number: "))
second = int(input("Second number: "))
for i in range(first, second + 1):
    print(i)

print("---")

first = int(input("First number: "))
second = int(input("Second number: "))
for i in range(first, second + 1):
    print(f"1. All numbers in range")
    print(f"2. All numbers divisible by 3")
    print(f"3. All numbers divisible by 7")
    print(f"4. Count of numbers divisible by 5")
    break

print("---")

first = int(input("First number: "))
second = int(input("Second number: "))
for i in range(first, second + 1):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print("---")

first = int(input("First number: "))
second = int(input("Second number: "))
for i in range(first, second + 1):
    if i % 2 == 0:
        print("Even:", i)
    else:
        print("Odd:", i)

print("---")

first = int(input("First number: "))
second = int(input("Second number: "))
for i in range(first, second + 1):
    if i % 6 == 0 and i != 6:
        print(i)

print("---")

a = int(input("Enter A: "))
n = int(input("Enter N: "))
result = a ** n
print(f"{a} to the power of {n} = {result}")
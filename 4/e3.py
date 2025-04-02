a = int(input())
b = int(input())

while a * b != 0:
    a, b = b, a % b
print(a + b)
def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

a = int(input())
b = int(input())
ans = gcd(a, b)
print(f'НОД чисел {a} и {b} равен {ans}')
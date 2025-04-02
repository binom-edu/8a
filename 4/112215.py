n = int(input())

while n > 9:
    d1 = n % 10
    d2 = n // 10 % 10
    if d1 != d2:
        print('NO')
        break
    n //= 10
else:
    print('YES')
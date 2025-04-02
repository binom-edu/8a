n = int(input())

while n > 0:
    if n % 10 == n // 10 % 10:
        print('YES')
        break
    n //= 10
else:
    print('NO')
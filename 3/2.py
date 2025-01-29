n = int(input())

d4 = n % 4 == 0
d100 = n % 100 == 0
d400 = n % 400 == 0

if (d4 and (not d100)) or d400:
    print('YES')
else:
    print('NO')
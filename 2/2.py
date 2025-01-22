a = int(input())
b = int(input())
c = int(input())

# Максимум из трех чисел

ans = a
if b > ans:
    ans = b

if c > ans:
    ans = c

print(ans)
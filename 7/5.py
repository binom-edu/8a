import random
n = 3
a = [random.randint(-10, 10) for i in range(n)]
print(a)

# максимальный элемент
ans = -11
for x in a:
    if x > ans:
        ans = x
print(ans)
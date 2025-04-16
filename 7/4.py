import random
n = 3
a = [random.randint(-10, 10) for i in range(n)]
print(a)

# количество положительных элементов
ans = 0
for x in a:
    if x > 0:
        ans += 1
print(ans)
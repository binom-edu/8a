import random
n = 3
a = [random.randint(-10, 10) for i in range(n)]
print(a)

# посчитать количество пар соседних по индексу элементов, имеющих разные знаки
ans = 0
for i in range(n - 1):
    x, y = a[i], a[i + 1]
    # if (x > 0 and y < 0) or (x < 0 and y > 0):
    if x * y < 0:
        ans += 1
print(ans)
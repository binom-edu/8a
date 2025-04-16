import random
n = 3
a = [random.randint(-10, 10) for i in range(n)]
print(a)

# сумма элементов
ans = 0
for x in a:
    ans += x
print(ans)
print(sum(a))
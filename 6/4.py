a = []
for i in range(5):
    a.append(i)
print(a)

b = [i for i in range(5)]
print(b)
c = [i ** 2 for i in range(10)]
print(c)
d = [i for i in c if i % 10 == 6]
print(d)
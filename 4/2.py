c = 0
while c < 10:
    if c == 3:
        c += 1
        continue
    print(c)
    if c == 6:
        break
    c += 1
else:
    print('Блок else')
print('Конец программы')
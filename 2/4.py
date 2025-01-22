a = int(input())
b = int(input())

# Какое из чисел больше. Вложенное ветвление
if a > b:
    print('Первое больше')
else:
    if a == b:
        print('Равны')
    else:
        print('Второе больше')
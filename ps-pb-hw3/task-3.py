quantity = 0
summ = 0
previous = 0
current = 1
while current<10**7:
    if current % 2 == 0:
        print(current, end='  ')
        summ +=current
    quantity +=1
    temp = current
    current +=previous
    previous = temp

print()
print(f'Количество элементов последовательности: {quantity}')
print(f'Сумма всех чётных элементов последовательности: {summ}')
print(f'Предпоследнее число заданной последовательности: {previous}')
# Последним считаем число, которое уже не меньше 10000000

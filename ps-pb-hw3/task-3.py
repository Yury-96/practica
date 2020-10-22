quantity = 0
summ = 0
previous = 0
current = 1
while current<10**7:
    quantity +=1
    print(current, end='  ')
    temp = current
    current +=previous
    previous = temp
    if current % 2 == 0 and current<10**7:
        summ +=current
        #print(current, end='  ')
print()
print(f'Количество элементов последовательности: {quantity}')
print(f'Сумма всех чётных элементов последовательности: {summ}')
print(f'Предпоследнее число заданной последовательности: {previous}')

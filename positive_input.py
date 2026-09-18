a = 0

while True:
  num = int(input('Введите число: '))
  if num > 0:
    break
  a += 1

# Вывод результатов
print('Квадрат числа:', num**2)
print('Количество отклонённых попыток:', a)
n = int(input('Введите кол-во чисел: '))

count = 0
total_sum = 0

for _ in range(n):
  num = int(input('Введите число: '))
  if num % 3 == 0:
    count += 1
    total_sum += num

print('=' * 40)
print('Количество:', count)
print('Сумма:', total_sum)
print('=' * 40)

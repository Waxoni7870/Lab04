n = int(input())

first = int(input())
total_sum = first
positive_count = 1 if first > 0 else 0
maximum = first

for _ in range(n - 1):
  num = int(input())
  total_sum += num
  if num > 0:
    positive_count += 1
  if num > maximum:
    maximum = num

print('Сумма:', total_sum)
print('Количество положительных:', positive_count)
print('Максимум:', maximum)
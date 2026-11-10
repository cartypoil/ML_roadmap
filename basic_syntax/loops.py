# 1. Обычный цикл for и функция range()
# range(старт, стоп, шаг)
print('1. Простой цикл for и range')

for number in range(1, 6):
    print('Число:', number)

for count in range(5, 0, -1):
    print('Обратный отсчет:', count)


# 2. Цикл while, операторы break и continue
print('\n2. Цикл while, break и continue')

counter = 0
total_sum = 0

while counter < 10:
    counter += 1

    # continue сразу переходит на следующий круг, пропуская код ниже
    if counter % 2 != 0:
        continue

    total_sum += counter
    print(f'Прибавили {counter}, текущая сумма: {total_sum}')

    # break полностью обрывает цикл
    if total_sum >= 12:
        print('Сумма 12, выходим из цикла')
        break
print(total_sum)


# 3. Конструкция for else
# Блок else срабатывает только если цикл закончился сам
print('\n3. Поиск элемента через for-else')

data_values = [14, 21, 36, 42, 9, 28]
target_divisor = 5

for value in data_values:
    if value % target_divisor == 0:
        print(f'Найдено число {value}, кратное {target_divisor}')
        break
else:
    # Этот блок сработает, если ни одно число не подошло
    print(f'Чисел, кратных {target_divisor}, в списке не нашлось')


# 4. Нумерация элементов через enumerate()
# Избавляет от ручного счетчика i = 0 и i += 1
print('\n4. Использование enumerate')

actions = ['прочитать', 'перевести', 'записать']

# start=1 задает номер с единицы, а не с нуля
for step, action in enumerate(actions, start=1):
    print(f'Шаг {step}: делаем действие {action}')


# 5. zip()
# Связывает элементы из нескольких списков
# Цикл идет до тех пор, пока не кончится самый короткий список.
print('\n5. zip')

students = ['Алексей', 'Дмитрий', 'Елена', 'Анатолий']
scores = [85, 92, 78]

for name, score in zip(students, scores):
    print(f'Студент: {name}, результат: {score} баллов')


# 6. Ошибка при удалении элементов во время цикла

numbers = [1, 2, 3, 4, 5, 6]

# Если удалять числа прямо во время цикла:
# список сдвинется влево, а цикл перешагнет через соседнее число.

# Способ 1: собрать нужные числа в новый список
odds = [num for num in numbers if num % 2 != 0]
print('Только нечетные через генератор:', odds)

# Способ 2: шагать по копии списка через срез numbers[:], а удалять из оригинала
for n in numbers[:]:
    if n % 2 == 0:
        numbers.remove(n)

print('Очищенный оригинальный список:', numbers)


# 7. Разворот списка через reversed()
# numbers[::-1] сначала создает в памяти полную копию списка в развернутом виде.
# reversed() не тратит память на копирование, а просто читает оригинал с конца.
print('\n7. Разворот списка через reversed')

steps = ['step 1', 'step 2', 'step 3']

for step in reversed(steps):
    print('Откат шага:', step)

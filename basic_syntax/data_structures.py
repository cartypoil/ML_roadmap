
# 1. Списки(list)

# Базовые операции
fruits = ['apple', 'banana', 'orange', 'banana']
fruits.append('mango')
fruits[1] = 'cherry'

# Разница remote и pop
fruits.remove('banana') # Удаляет первое совпадение

# Удаляем и помещаем в переменную
last_fruit = fruits.pop()
first_fruit = fruits.pop(0)

print(f'Забрали с начала: {first_fruit}, забрали с конца: {last_fruit}')
print(f'Осталось {fruits}\n')


# 2. Генераторы списков
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]

print('Генераторы списков:', squares, '\n')


# 3. Кортежи(tuple) - неизменяеммые структуры
resolution = (1920, 1080)
# resolution[0] = 1 # TypeError: 'tuple' object does not support item assignment
width, height = resolution # Распаковка сразу по переменным
print(f'Кортеж - {resolution} ширина: {width}, высота: {height}\n')

# 4. Словари(dict) - пары ключ: значение
human = {
    'name': 'nikita',
    'age': 18,
    'role': 'student'
}

# Добавление и изменение данных
human['height'] = 183
human['age'] = 18.5

# Безопастное чтение через get: если нет ключа ошибки не будет
w = human.get('width', 60)

print(f'Человек: {human}')
print(f'Вес человека: {w}\n')


# Множества(set) - не повторяющиеся элементы без порядка

animals = ['dog', 'cat', 'bird', 'cat', 'dog']
animals_set = set(animals) # Приведение к множеству(удаление дубликатов)

stop_char = {'a', 'b', 'c', 'd', 'e'}
print(f'Множество: {animals_set}')
print(f'Мнгновенная проверка a в stop_char:', 'a' in stop_char, '\n')

# Операции с множествами
skills = {'python', 'git'}
request = {'python', 'sql', 'docker'}

print('Есть то, что требуется', skills&request)
print('Нужно выучить', request-skills)





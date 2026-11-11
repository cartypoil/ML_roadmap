# 1. Базовая функция и возврат значения через return
# return отдает результат в переменную, а не просто печатает на экран
def calc_square(x):
    return x * x

res = calc_square(4)
print('Квадрат числа:', res)


# 2. Несколько параметров и дефолтные значения
# discount=10 сработает, если скидку не передали при вызове
def get_final_price(price, discount=10):
    return price - (price * discount / 100)

price_1 = get_final_price(1000)      # скидка 10% по умолчанию
price_2 = get_final_price(1000, 25)  # скидка 25%
print('Цена 1:', price_1)
print('Цена 2:', price_2)


# 3. Вызов по именам аргументов
def create_profile(name, role):
    return f'Пользователь: {name}, роль: {role}'

# Можно менять порядок, если указывать имена
info = create_profile(role='admin', name='alex')
print(info)


# 4. Возврат нескольких значений сразу
# Python упаковывает их в кортеж, который можно сразу распаковать
def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [15, 2, 42, 8, 99, 4]
low, high = get_min_max(nums)
print('Минимум:', low, 'Максимум:', high)


# 5. Локальные и глобальные переменные
# Переменная внутри функции видна только внутри нее
step = 2

def add_step(val):
    result = val + step  # step берется снаружи, result живет только тут
    return result

print('Сумма с шагом:', add_step(10))


# 6. Полезные встроенные функции (Built-in)
data = [12, -5, 8, 0, -20, 15]

# sum, min, max
print('Сумма элементов:', sum(data))
print('Минимальный:', min(data))
print('Максимальный:', max(data))

# abs - модуль числа
print('Модуль -5:', abs(-5))

# round - округление
pi_val = 3.14159
print('Округление до 2 знаков:', round(pi_val, 2))

# sorted - сортирует и отдает новый список, не меняя старый
sorted_data = sorted(data)
print('Отсортированный список:', sorted_data)
print('Оригинал остался целым:', data)
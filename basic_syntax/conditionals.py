# 1. Базовая конструкция if, elif, else
# elif проверяет условие, только если предыдущий if не сработал
score = 82

if score >= 90:
    grade = 5
elif score >= 75:
    grade = 4
elif score >= 60:
    grade = 3
else:
    grade = 2

print('Оценка за тест:', grade)


# 2. Цепочки сравнений
# Можно не писать score >= 10 and score <= 100, а писать как в математике
age = 22

if 18 <= age < 45:
    print('Возраст подходит')


# 3. Логические операторы and, or, not
# and требует истинности обоих условий, or - хотя бы одного
has_access = True
is_blocked = False

if has_access and not is_blocked:
    print('Доступ открыт')

status_code = 404
if status_code == 400 or status_code == 404:
    print('Ошибка на стороне клиента')


# 4. Проверка на пустоту (Truthy и Falsy)
# Ноль, None, пустые списки [], строки "" и словари {} считаются False
# Не надо писать len(data) == 0 или text != ""
data = []

if not data:
    print('Список данных пуст')

username = 'nk'
if username:
    print('Имя пользователя задано:', username)


# 5. Тернарный оператор (условие в одну строку)
num = 7

parity = 'четное' if num % 2 == 0 else 'нечетное'
print(f'Число {num} — {parity}')


# 6. Проверка наличия через in и not in
allowed = ['admin', 'moderator']
current = 'guest'

if current in allowed:
    print('Доступ разрешен')
else:
    print('Нет прав доступа')


# 7. pass
# В Python нельзя оставить блок if пустым, иначе вылетит ошибка отступа
debug_mode = False

if debug_mode:
    pass  # можно дописать позже
else:
    print('Все работает')
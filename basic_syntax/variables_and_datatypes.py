
x = 5
y = x

# У переменных одна и та же ячейка
print(id(x), id(y))

# Базовые типы данных
fl = 0.1 # float
i = 1 # int
st = 'Истинность' # str
is_true = True # bool
n = None # NoneType

print(type(i).__name__)
print(f'{st}: {is_true}')

# Особенность float 0.1 + 0.2, ошибка из-за округления
print(f'0.1+0.2=0.3: ', 0.1+0.2==0.3)
print(0.1 + 0.2)

# Множественное присвасваивание и обмен
a, b = 3, 4
print(a, b)
a, b = b, a
print(a, b)

# задание 3
from package.math import add, multiply
from package.string import word_count
a=int(input('введите число:'))
b=int(input('введите число:'))
w=input('введите слова:')

ad=add(a,b)
m=multiply(a,b)
wo=word_count(w)
print(f"Сумма: {ad}")
print(f'произведение:{m}')
print(f"кол-во слов:{wo}")

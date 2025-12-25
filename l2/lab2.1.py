
def greet(name):
    return f"Hello, {name}"
print(greet(input("Имя:")))

def square(number):
    return number**2
print(square(int(input("Введите число: "))))

def max_of_two(x, y):
    if x > y:
        return x
    elif x == y:
        return "Ошибка"
    else:
        return y
print(max_of_two(int(input("Введите число 1: ")), int(input("Введите число 2: "))))
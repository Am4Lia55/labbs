def is_prime(number):
    if number <= 1:
        return "Число непростое"
    for i in range(2, number):
        if number % i == 0:
            return "Число непростое"
    return "Число простое"
print(is_prime(int(input("Введите число"))))
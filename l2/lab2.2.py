def describe_person(name, age=30):
    return f"Имя: {name} Возраст: {age}"
name = input()
age = input()
if age:
    print(describe_person(name, age))
else:
    print(describe_person(name))
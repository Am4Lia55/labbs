def read_all(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content=f.read()
            print(content)
    except FileNotFoundError:
        print('файл не найден')
def read_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                print(line)
    except FileNotFoundError:
        print('файл не найден')
print('1-читать весь файл')
print('2-читать файл построчно')
choice = input('выберите')
filename = input('выберите файл')
if choice == '1':
    read_all(filename)
elif choice == '2':
    read_lines(filename)
else:
    print('ошибка')


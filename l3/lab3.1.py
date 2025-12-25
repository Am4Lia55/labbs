def read_all(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()
def read_lines(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line)
    return lines
filename = 'example.txt'
print('1-читать весь файл')
print('2-читать файл построчно')
choice = input('выберите')
if choice == '1':
    content= read_all(filename)
    print(content)
elif choice == '2':
    lines= read_lines(filename)
    for line in lines:
        print(line)
else:
    print('ошибка')


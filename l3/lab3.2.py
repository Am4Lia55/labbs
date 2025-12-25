def write_user_input(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    return ('файл создан')
def append_text(filename, content):
    with open(filename, 'a') as f:
        f.write('\n' + content)
    return ('текст добавлен')
print('1-записать новый файл')
print('2-добавить в файл')
choice=input('выберите')
filename=input('введите имя файла')
text=input('ввести')
if choice == '1':
    print(write_user_input(filename, text))
elif choice == '2':
    print(append_text(filename, text))
else:
    print('ошибка')


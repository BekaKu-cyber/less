import os

dir_name = "read.py"

def show_file_list():
    d = os.listdir(dir_name)
    files_exist = False
    for i, file in enumerate(d):
        files_exist = True
        print(i, ':', file)
    if not files_exist:
        print('Файлов пока нет')

def add_new_record():
    name = input('Введите имя')
    surname = input('Введите фамилию')
    d = {
        'name': name,
        'surname': surname
    }
    json_str = json.dumps(d)
    f_name = d['name'] + '.txt'
    papka = os.listdir(dir_name)
    if f_name in papka:
        f_name = '1_' + f_name

    full_filename = dir_name + '/' +  f_name
    with open(full_filename, 'w') as f:
        print(f)
        f.write(json_str)



def view_record(index):
    print('тут мы будем отображать файл c индексом ', index)
    d = os.listdir(dir_name)
    filename = None
    for i, file in enumerate(d):
        if i == int(index):
            filename = file
    if filename:
        print('here we open file', filename)
        with open(dir_name + '/' + filename, 'r') as f:
            file_content = f.read()
            saved_dict = json.loads(file_content)
            print('Сохраненный словарь', saved_dict)

while True:
    vvod = input('Введите команду: [list, add, exit или индекс записи для просмотра: ')
    if vvod == 'list':
        show_file_list()
    elif vvod == 'add':
        add_new_record()
    elif vvod == 'exit':
        break;
    else:
        view_record(vvod)
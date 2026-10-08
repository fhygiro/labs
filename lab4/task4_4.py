import os
import shutil

GUIDE = {
    'dir': 'открыть директорию',
    'copy': 'копировать файл (файл текущей директории?новая директория)',
    'rename': 'переименовать (rename старое-имя/новое-имя)',
    'delete': 'удалить файл',
    'list': 'просмотреть директорию',
    'mkdr': 'создать папку'
}

cur_dir = ''

def copy(string):
    old = f'{cur_dir}/{string.split("?")[0]}'
    new = string.split('?')[1]
    if os.path.isfile(old) and os.path.isdir(new):
        shutil.copy(old, new)
    else:
        print('Ошибка')

def mkdr(name):
    if not os.path.isdir(f'{cur_dir}/{name}'):
        os.mkdir(f'{cur_dir}/{name}')
    else:
        print('Директория уже существует!')

def open_dir(path):
    if os.path.isdir(path):
        global cur_dir
        cur_dir = path

def list_dir(dir):
    for element in os.listdir(dir):
        print(element)

def rename(string):
    old = f'{cur_dir}/{string.split("/")[0]}'
    new = f'{cur_dir}/{string.split("/")[1]}'
    if os.path.isdir(old) or os.path.isfile(old):
        os.rename(old, new)
    else:
        print('Файл или директория не найдена')

def delete(element):
    path = f'{cur_dir}/{element}'
    if os.path.isfile(path):
        os.remove(path)
    else:
        print('Файл не найден')

def parser(string):
    try:
        command = string.split()[0]
        if command == 'dir':
            open_dir(string.split()[1])

        elif command == 'list':
            if len(string.split()) == 1:
                list_dir(cur_dir)
            else:
                list_dir(string.split()[1])

        elif command == 'rename':
            rename(string.split()[1])

        elif command == 'delete':
            delete(string.split()[1])

        elif command == 'mkdr':
            mkdr(string.split()[1])

        elif command == 'copy':
            copy(string.split()[1])
    except:
        pass

def init_guide():
    for k, v in GUIDE.items():
        print(f'{k}  --  {v}')
    print('-'*60, end='\n\n\n')

def main():
    init_guide()

    while True:
        command = input(f'{cur_dir} :> ')
        parser(command)

if __name__ == "__main__":
     main()
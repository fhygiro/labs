from tkinter import *
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText

window = Tk()
window.title('Шифроватор Цезаря и Виженера')
window.geometry('500x550')
window.resizable(False, False)

ALPH = [i for i in sorted('йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')]
mode = 'activate'

def key_unhide():
    key_label.grid(row=9, column=1, pady=(15, 0))
    key_ent.grid(row=10, column=1)
    
def key_hide():
    key_label.grid_forget()
    key_ent.grid_forget()

def mode_changer(event):
    global mode
    if modes.get() == 'Зашифровка': mode = 'activate'
    elif modes.get() == 'Расшифровка': mode = 'deactivate'

def run():
    result.delete('1.0', 'end')
    if method.get() == 'cesar': cesar(10)
    elif method.get() == 'vigenere': vigenere(key_ent.get())

def vigenere(key):
    text = usr_text.get('1.0', 'end')
    res = ''

    c = 0
    i = 0
    while c <= len(text) - 2:
        if i > len(key) - 1: i = 0

        if text[c] in ALPH:
            index_char = ALPH.index(text[c])
            index_key = ALPH.index(key[i])
            if mode == 'activate':
                flag = index_char + index_key
                if flag + 1 > len(ALPH): flag = index_key - (len(ALPH) - index_char)
            elif mode == 'deactivate':
                flag = index_char - index_key
                if flag < 0: flag = len(ALPH) - abs(index_char - index_key)
            res+=ALPH[flag]
        else:
            res+=text[c]
        c+=1
        i+=1
    result.insert(INSERT, res)

def cesar(jump):
    text = usr_text.get('1.0', 'end')
    res = ''

    for c in text:
        if c in ALPH:
            if mode == 'activate':
                flag = ALPH.index(c) + jump
                if flag + 1 > len(ALPH): flag = jump - (len(ALPH) - ALPH.index(c))
            elif mode == 'deactivate':
                flag = ALPH.index(c) - jump
                if flag < 0: flag = len(ALPH) - abs(ALPH.index(c) - jump)
            res+=ALPH[flag]
        else:
            res+=c

    result.insert(INSERT, res)

frame = Frame(
    window,
    padx = 20,
    pady = 20,
)

frame.pack(fill=Y)

first_label = Label(
    frame,
    text = 'Начальная строка: ',
    font = 20
)

second_label = Label(
    frame,
    text = 'Результат: ',
    font=20
)

usr_text = ScrolledText(
    frame,
    width = 50,
    height = 5
)

result = ScrolledText(
    frame,
    width = 50,
    height = 5
)

button = Button(
    frame,
    width = 30,
    height = 3,
    text = 'Перевести',
    command = lambda: run()
)

modes = Combobox(
    frame,
    values = [
        'Зашифровка',
        'Расшифровка'
    ],
    state = "readonly"
)

modes.set('Зашифровка')
modes.bind('<<ComboboxSelected>>', mode_changer)

method = StringVar(value='cesar')

cesar_rb = Radiobutton(
    frame,
    text = 'Метод Цезаря',
    value = 'cesar',
    variable = method,
    command = lambda: key_hide()
)

vigenere_rb = Radiobutton(
    frame,
    text = 'Метод Вижинера',
    value = 'vigenere',
    variable = method,
    command = lambda: key_unhide()
)

key_label = Label(
    frame,
    font = 20,
    text = 'Ключ'
)

key_ent = Entry(
    frame,
    width =50
)

modes.grid(row=1, column=1)
first_label.grid(row=2, column=1, pady=(25, 0))
usr_text.grid(row=3, column=1)
button.grid(row=4, column=1, pady=(25, 0))
second_label.grid(row=5, column=1, pady=(25, 0))
result.grid(row=6, column=1)
cesar_rb.grid(row=7, column=1, pady=(20, 5))
vigenere_rb.grid(row=8, column=1)

window.mainloop()
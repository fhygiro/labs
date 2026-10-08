from zipfile import ZipFile
from tkinter import *
from tkinter import filedialog

window = Tk()
window.title('Резервное копирование')
window.geometry('1000x500')
window.resizable(False, False)


path = ''
path_to_save = ''

def select_dir():
    global path
    dir_path = filedialog.askdirectory()
    if dir_path:
        path = dir_path
        select_dir_label['text'] = f'Папка для архивирования: {path}'

def select_dir_to_save():
    global path_to_save
    dir_path = filedialog.askdirectory()
    if dir_path:
        path_to_save = dir_path
        select_dir_to_save_label['text'] = f'Путь для архивирования: {path_to_save}'

frame = Frame(
    window,
    padx=20,
    pady=20
)

timer_frame = Frame(
    frame,
    padx=20,
    pady=20
)

select_dir_label = Label(
    frame,
    text = 'Папка для архивирования: ',
    font = 20
)

select_dir_to_save_label = Label(
    frame,
    text = 'Путь для архивирования: ',
    font = 20
)

timer_label = Label(
    timer_frame,
    text = 'Таймер: ',
    font = 20
)

hour_spinbox = Spinbox(
    timer_frame,
    from_ = 0,
    to = 24,
    increment = 1
)

minute_spinbox = Spinbox(
    timer_frame,
    from_ = 0,
    to = 59,
    increment = 1
)

select_dir_button = Button(
    frame,
    text = 'Выбрать папку',
    command = lambda: select_dir()
)

select_dir_to_save_button = Button(
    frame,
    text = 'Выбрать папку',
    command = lambda: select_dir_to_save()
)

minute_label = Label(
    timer_frame,
    text = 'Минуты'
)

hour_label = Label(
    timer_frame,
    text = 'Часы'
)

frame.pack(fill=X)

select_dir_button.grid(row=1, column=0)
select_dir_label.grid(row=1, column=1)

select_dir_to_save_button.grid(row=2, column=0)
select_dir_to_save_label.grid(row=2, column=1)

timer_label.pack()

minute_label.pack()
minute_spinbox.pack()
hour_label.pack()
hour_spinbox.pack()

window.mainloop()
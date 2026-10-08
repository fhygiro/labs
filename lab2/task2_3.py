from tkinter import *
from tkinter.ttk import Combobox 

window = Tk()
window.title('Калькулятор')
window.geometry('250x500')
window.resizable(False, False)

def calc(event):
    selection = methods.get()
    try:
        if selection == '+':
            result_label['text'] = f'Результат: {float(first_ent.get()) + float(second_ent.get())}'
        elif selection == '-':
            result_label['text'] = f'Результат: {float(first_ent.get()) - float(second_ent.get())}'
        elif selection == '*':
            result_label['text'] = f'Результат: {float(first_ent.get()) * float(second_ent.get())}'
        elif selection == '/':
            result_label['text'] = f'Результат: {float(first_ent.get()) / float(second_ent.get())}'
    except ZeroDivisionError:
        result_label['text'] = 'Делить на 0 нельзя!'
    except:
        result_label['text'] = 'Введите числа!'
        first_ent.delete(0, END)
        second_ent.delete(0, END)

def clear(event):
    result_label['text'] = ''

frame = Frame(
   window
)

frame.pack(fill=Y)

first_num_label = Label(
    frame,
    text = 'Первое число',
    font = 20
)

second_num_label = Label(
    frame,
    text = 'Второе число',
    font = 20
)

methods_label = Label(
    frame,
    text = 'Операция',
    font = 20,
)

result_label = Label(
    frame,
    text = '',
    font = 25
)

methods = Combobox(
    frame, 
    values = ['+', '-', '*', '/'], 
    width = 20, 
    state = "readonly"
)

first_ent = Entry(frame)
second_ent = Entry(frame)

methods.bind("<<ComboboxSelected>>", calc)
first_ent.bind('<FocusIn>', clear)

first_num_label.grid(row=1, column=1, pady=(50, 0))
first_ent.grid(row=2, column=1)
second_num_label.grid(row=3, column=1, pady=(50, 0))
second_ent.grid(row=4, column=1)
methods_label.grid(row=5, column=1, pady=(50, 0))
methods.grid(row=6, column=1)
result_label.grid(row=7, column=1, pady=(70, 0))

window.mainloop()
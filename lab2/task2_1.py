a = input('Введите строку: ').lower().replace(' ', '')
r = len(set([i for i in a]))
print(f'Уникальных символов: {r}')
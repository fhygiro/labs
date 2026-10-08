s = input('Введите строку: ')
a = s.split()
print(sorted(a, key=len))
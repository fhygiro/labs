def from_dec_to_another(num, to_num):
    alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''

    if num == 0:
        return '0'

    while num > 0:
        res += alph[num % to_num]
        num //= to_num
    return res[::-1]

while True:
    try:
        num = input('\nВведите число: ').upper()
        ns1 = int(input('Введите систему счисления: '))
        ns2 = int(input('Введите систему счисления результата: '))

        while ns1 > 36 or ns2 > 36 or ns2 < 2 or ns1 < 2:
            print('Система счисления может принимать значение от 2 до 36')
            ns1 = int(input('Введите систему счисления: '))
            ns2 = int(input('Введите систему счисления результата: '))

    except ValueError:
        print('Система счисления должна содержать только цифры!')
        continue
    
    try:
        result = from_dec_to_another(int(num, ns1), ns2)
    except ValueError:
        print('Число не может быть записано в этой системе счисления')
        continue
    
    print(f'Результат - {result}')
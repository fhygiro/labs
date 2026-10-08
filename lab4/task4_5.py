def xor_coding(text, key):
    key_bin = key.encode('utf-8')
    text_bin = text.encode('utf-8')

    while len(key_bin) < len(text_bin):
        i = len(text_bin)-len(key_bin)
        key_bin += key_bin[:i]
    
    if len(key_bin) > len(text_bin):
        key_bin = key_bin[:len(text_bin)]
    
    result = bytearray([text_bin[i] ^ key_bin[i] for i in range(len(key_bin))]).hex()
    return result


def xor_uncoding(text, key):
    text_bin = bytes.fromhex(text)
    key_bin = key.encode('utf-8')

    while len(key_bin) < len(text_bin):
        i = len(text_bin)-len(key_bin)
        key_bin += key_bin[:i]
    
    if len(key_bin) > len(text_bin):
        key_bin = key_bin[:len(text_bin)]

    result = bytearray([text_bin[i] ^ key_bin[i] for i in range(len(key_bin))])
    return result.decode('utf-8')


while True:
    mode = input('Шифрование (C), дешифрование (U): ')
    if mode == 'C':
        text = input('Текст для шифрования: ')

        while True:
            key = input('Ключ: ')
            if len(key) > 0:
                break
            print('Ключ не может быть пустым')

        print(f'Зашифрованный текст: {xor_coding(text, key)}', end='\n\n')

    elif mode == 'U':
        text = input('Текст для дешифрования: ')

        while True:
            key = input('Ключ: ')
            if len(key) > 0:
                break
            print('Ключ не может быть пустым')
            
        print(f'Дешифрованный текст: {xor_uncoding(text, key)}', end='\n\n')
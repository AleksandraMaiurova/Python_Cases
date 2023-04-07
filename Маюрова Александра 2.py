number = input()
if len(number) != 1:
    print('Ошибка - необходимо ввести один символ.')
else:
    n = ord(number)
    print(bin(n), oct(n), n, hex(n))
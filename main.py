import random

chars = 'abcdefghijkln'
number = input('Количество всех паролей'+ "\n")
length = input('Длина пароля?'+ "\n")
number = int(number)
length = int(length)
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)

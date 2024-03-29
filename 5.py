# Компьютерная программа "Шахматы с Гарри Каспаровым" делает ход конем.
# Проверьте правильность ее хода.

coordinates = input('Введите начальные и конечные координаты через тире: ')

num_1 = int(coordinates[1])
num_2 = int(coordinates[4])

letter_1 = ord(coordinates[0])
letter_2 = ord(coordinates[3])

if ((abs(num_1 - num_2) == 2 and abs(letter_1 - letter_2) == 1)
or (abs(num_1 - num_2) == 1 and abs(letter_1 - letter_2) == 2)):
    print('верно')
else:
    print('неверно')
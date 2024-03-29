# Напишите программу, определяющую цвет клетки шахматного поля.

coordinates = input('Введите координаты шахматной клетки: ')
number = int(coordinates[1])

def converter(letter):
    letter = coordinates[0]
    match letter:
        case 'a':
            value = 1
        case 'b':
            value = 2
        case 'c':
            value = 3
        case 'd':
            value = 4
        case 'e':
            value = 5
        case 'f':
            value = 6
        case 'g':
            value = 7
        case 'h':
            value = 8
        case _:
            value = -1
    return value

letter_1 = converter(coordinates[0])
if (number % 2 == 0 and letter_1 % 2 == 0) or (number % 2 != 0 and letter_1 % 2 != 0):
    print('черный')
else:
    print('белый')
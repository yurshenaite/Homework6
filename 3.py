# Район Барселоны Эшампле представляется в виде прямоугольных кварталов.
# Для обеспечения правопорядка, в один из праздников, полиция выполнила оцепление района N x M кварталов.
# Если полностью перекрыть движение по одной из улиц внутри оцепления, сможет ли полиция отделить ровно К кварталов?

n, m = map(int, input('Введите размер района в формате NxM: ').split('x'))
k = int(input('Сколько кварталов нужно отделить?: '))

if (n * m) % 2 == 0:
    if ((n * m) - k) % 2 == 0:
        print('успешно')
    else:
        print('неосуществимо')
elif (((n * m) - k) % n == 0) or (((n * m) - k) % k == 0):
    print('успешно')
else:
    print('неосуществимо')
number = int(input('Введите номер вашего места: '))

if number > 36 and number < 55:
    print('Ваше место - боковое')
elif number < 36 and number > 0:
    print('Ваше место - купе')

if number%2==0 and number > 0 and number < 55:
    print('Ваше место - верхнее')
elif number%2==1 and number > 0 and number < 55:
    print('Ваше место - нижнее')

if number < 1 or number > 54:
    print ('Снаружи ехать собрался?')

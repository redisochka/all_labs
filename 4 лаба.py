def z1():

    number = int(input('Введите число: '))
    if number % 3 == 0:
        print('Число',number,'делится на 3\n')
    else:
        print('Число',number,' не делится на 3\n')

def z2():

    try:
        number = int(input('Введите число: '))
        result = 100 / number
    except ValueError:
        print('Число, а не буквы...\n')
    except ZeroDivisionError:
        print('Делить на ноль нельзя!\n')
    else:
        print('Ответ: ',result,'\n')

def z3():

    import time

    date = input('Введите дату в формате дд/мм/гггг: ')
    try:
        invalid_date = time.strptime(date, '%d/%m/%Y')
    except ValueError:
        print('Неправильно введена дата!\n')
    else:
        year = int(date[8:])
        day = int(date[0:2])
        month = int(date[3:5])
        sum = day * month

        if sum == year:
            print('Дата магическая! Поздравляю! :D\n')
            return True
        else:
            print('Дата не магическая ;(\n')
            return False

def z4():

    date = input('Введите номер билета: ')
    sum1 = 0
    sum2 = 0
    if len(date) % 2 != 0:
        print('Номер должен быть четным!\n')
    else:
        number = int(len(date) / 2)
        half1 = (date[0:number])
        half2 = (date[number:])

        for x in half1:
            sum1 = int(x) + sum1

        for x in half2:
            sum2 = int(x) + sum2

        if sum1 == sum2:
            print('Ваш билет счастливый! :D\n')
        else:
            print('Ваш билет не счастливый! :(\n')


z1()
z2()
z3()
z4()
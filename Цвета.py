Color1 = input('Введите первый цвет: ')
Color2 = input('Введите второй цвет: ')

if Color1 != "Красный" and Color1 != "Синий" and Color1 != "Желтый":
    print ('С большой буквы и всего 3 цвета, ДУМАЙ, МАРК!')
if Color2 != "Красный" and Color2 != "Синий" and Color2 != "Желтый":
    print('С большой буквы и всего 3 цвета, ДУМАЙ, МАРК!')

if Color1 == 'Красный' and Color2 == 'Красный':
    print('Получится - Красный')
if Color1 == 'Синий' and Color2 == 'Синий':
    print('Получится - Синий')
if Color1 == 'Желтый' and Color2 == 'Желтый':
    print('Получится - Желтый')
if Color1 == 'Красный' and Color2 == 'Синий':
    print('Получится - Фиолетовый')
if Color1 == 'Синий' and Color2 == 'Красный':
    print('Получится - Фиолетовый')
if Color1 == 'Красный' and Color2 == 'Желтый':
    print('Получится - Оранжевый')
if Color1 == 'Желтый' and Color2 == 'Красный':
    print('Получится - Оранжевый')
if Color1 == 'Синий' and Color2 == 'Желтый':
    print('Получится - Зелёный')
if Color1 == 'Желтый' and Color2 == 'Синий':
    print('Получится - Зелёный')
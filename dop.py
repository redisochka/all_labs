import re
library = []
# Создание библиотеки
with open('synonyms.txt', 'r+') as file:
# Открытие на чтение и запись
    for line in file:
    # Для каждой строки в файле
        if line != "\n":
        # Если строка не пустая
            library.append([i.lower().strip().replace(';', '') for i in line.split() if i != '-'])
            # Для слов (i) если это не тире, добавь каждое в библиотеку применив низкий регистр, удалив пробелы с обоих сторон и поменяв двоеточие на пустоту
    wordbook = {}
    # Создание словаря
    for a in library:
    # Для каждой строки в библиотеке
        for b in a:
        # Для каждого слова в строке
            wordbook[b] = {c for c in a if c!=b}
            # К каждому слову (ключу) присваеваем другое слово в этой же строке, если оно не является самим собой


library = input('Введите слово: ').lower().strip()
# Прими слово, сделай ему нижний регистр и удали лишние пробелы, чтобы распознать как ключ
if wordbook.get(library) == None:
# Если такого слова (ключа) нет в словаре (d)
    print("Данное слово не найдено в словаре")
else:
    q = (str(wordbook.get(library))).replace("'","").replace(',',';')[1:-1]
    # Убираем лишнее и меняем запятые на двоеточие чтобы по веншую
    if q[-1] == ';':
    # Для избежания клонирования двоеточий при многократном прокруте
        q = q[0:-1]
    print('Найденные синонимы:',q)
    # Выдай слово по соответсвующему введенному слову (ключу), убрав фигурные скобки и кавычки
    answer = input("Предложенные варианты устраивают вас? Да/Нет ").lower().strip()
    # Прими да/нет, сделай ему нижний регистр и удали лишние пробелы
    if answer == "нет":
        word = input("Введите синоним который считаете подходящим: ")

        pattern = re.compile(q)
        # Грубо говоря ищет выражение внезависимости от наличия спец и мета символов
        with open('synonyms.txt', 'r+') as file:
        # Открытие на чтение и запись
            lines = file.readlines()
            # Считывает из файла все строки в список и возвращает его
            file.seek(0)
            # Смещает указатель в начало файла
            for line in lines:
                # Цикл перебирания строк
                result = pattern.search(line)
                # Поиск совпадения с выражением
                if result is None:
                    file.write(line)
                file.truncate()
                # Если кратко, то удаляет строку которая совпадет

        with open('synonyms.txt', 'a') as file:
        # Открытие на дозапись, информация добавляется в конец файла
            file.write(f"{library.capitalize()} - {word.lower().strip()}; {q}\n")
            # Напиши в файле изначальное слово с заглавной буквы и через тире напиши новое слово синоним + старые слова синонимы
            print("Синоним добавлен в словарь")


def z1():

    import random

    numbers = [random.randint(1, 10) for i in range(5)]
    user_number = int(input("Введите число от 1 до 10: "))

    if user_number in numbers:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")

    print("Исходный список:", numbers)
    print("Ваше число:", user_number)


def z2():

    my_list = [9, 7, 1, 1, 5, 8, 6]
    no_duplicates = list(set(my_list))
    if len(my_list) != len(no_duplicates):
        for value in no_duplicates:
            if my_list.count(value) > 1:
                print("Повторяющееся значение:", value)
    else:
        print("В списке нет повторяющихся значений.")

def z3():


    week_days = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')

    number_of_weekend_days = int(input("Сколько дней вы хотите отдыхать на выходных? "))
    weekend_days = ', '.join(week_days[-number_of_weekend_days:])
    work_days = ', '.join(week_days[:len(week_days) - number_of_weekend_days])

    print("Ваши выходные дни:", weekend_days)
    print("Ваши рабочие дни:", work_days)



def z4():


    import random

    group1 = ["Иванов", "Логинов", "Петренко", "Смирнов", "Кадыров", "Васильев", "Париев", "Аленик", "Дубровский",
              "Кузьмич"]
    group2 = ["Власов", "Пирогов", "Максимов", "Митсубишин", "Хохлов", "Прокофьев", "Бадров", "Киселев", "Харитонов",
              "Фуфелшмерцин"]

    team1 = random.sample(group1, 5)
    team2 = random.sample(group2, 5)

    team = tuple(team1 + team2)

    print("Группа 1:", group1)
    print("Группа 2:", group2)
    print("Спортивная команда:", team)

    print("Длина кортежа:", len(team))

    team_sorted = sorted(team)
    print("Сортированный кортеж:", team_sorted)

    if "Иванов" in team:
        print("Студент Иванов есть в команде.")
        print("Количество вхождений фамилии Иванов в команду:", team.count("Иванов"))
    else:
        print("Студент Иванов не найден в команде.")


z1()
z2()
z3()
z4()


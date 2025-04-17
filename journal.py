#Создать список студентов, где каждый студент хранится в виде кортежа
#Создать множество дисциплин в котором будут хранится уникальные ID каждого студента
#Реализовать функционал:
#1. Просмотр всех студентов
#2. Просмотр всех студентов на предмете
#3. Список предметов, которые посещает студент
#4. Какие студенты ходят сразу на все предметы

students = [
    (1, 'Egor', 20),
    (2, 'Petya', 19),
    (3, 'Katya', 21),
    (4, 'Kolya', 18)
]

physics = {1, 3, 4} #ID студентов
math = {1, 2, 3, 4}
russian = {2, 3, 4}

while True:
    answer = input('1 - список студентов, 2 - имена студентов на предмете, 3 - список предметов, которые посещает студент'
                   '4 - студенты, которые посещают все предметы'
                   '5 - добавить студента')

    if answer == '1':
        print(('id', 'name', 'age'))
        for i in students:
            print(i)
    elif answer == '2':
        subject = input('Выберите дисциплину (math, physics, russian)')
        if subject == 'math':
            for i in students: # - i - это отдельный студент из списка students
                if i[0] in math: #i[0] - ID студента
                    print(i[1]) #i[1] - имя студента
        elif subject == 'physics':
            for i in students:
                if i[0] in physics:
                    print(i[1])
        elif subject == 'russian':
            for i in students:
                if i[0] in russian:
                    print(i[1])
    elif answer == '3':
        name = input('Введите имя студента (Egor, Petya, Katya, Kolya) ')
        for i in students:
            if name == i[1]:
                print('Математика ', i[0] in math)
                print('Физика ', i[0] in physics)
                print('Русский язык ', i[0] in russian)

    elif answer == '4':
        inter1 = math.intersection(physics)
        print(inter1.intersection(russian))
    elif answer == '5':
        name = input('Как зовут?')
        age = int(input('Сколько лет?'))
        id = students[len(students) - 1][0] + 1
        students.append((id, name, age))
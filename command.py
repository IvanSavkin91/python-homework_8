
from ui import hello_user
from studens import students_list
from stunent_class import class_list

def search():
    while True:
        hello_user()
        n = int(input())
        if n ==1:
            with open('students.csv', 'r', encoding = 'utf_8') as f:
                    for line in f.readlines():
                        print(line)
            input('\nНажмите enter')

        elif n == 2:
            with open('class.csv', 'r', encoding = 'utf_8') as f:
                    for line in f.readlines():
                        print(line)
            input('\nНажмите enter')

        elif n == 3:
            answer = str(input('Введите фамилию ученика: '))
            if answer in students_list['Фамилия']:
                index = students_list['Фамилия'].index(answer)
            print(f"{students_list['ID'][index]}, {students_list['Имя'][index]} {students_list['Фамилия'][index]}, {students_list['Дата рождения'][index]}, {students_list['Успеваемость'][index]}")
            input('\nНажмите enter')
        
        elif n == 4:
            f = open('students.csv','a+', encoding = 'utf_8')
            new_contact = input('Введите данные(ФИ, год рождения, успеваемость, ID) ').split(' ')
            f.write('   |'.join(new_contact))
            f.close()
            print(f.readlines())
            # students_list['ID'] = new_contact[0]
            input('\nНажмите enter')

        elif n == 5:
            answer_name = input('Ввдите фамилию ученика: ')
            if answer_name in students_list['Фамилия']:
                index = students_list['Фамилия'].index(answer_name)
            print(f"Учник {students_list['Фамилия'][index]} {students_list['Имя'][index]} находится в кабинете {class_list['Кабинет'][index]} на уроке {class_list['Урок'][index]}, этаж {class_list['Этаж'][index]}")
            input('\nНажмите enter')


        elif n == 6:
            print('До встречи')
            exit()


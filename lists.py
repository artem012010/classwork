students = ['Смирнов', 'Иванов', 'Васильев', 'Молоткова', 'Алексашкина', 'Гришин']
students.sort()
amount_students = len(students)
i = 1
print('Список класса:')
for student in students:
    print(i, '-', student)
    i += 1
print('Всего учеников:', amount_students)


trips = ['эрмитаж', 'московский зоопарк', 'кремль', 'зоологический музей']
searching = input('Запрос:')
searching = searching.lower()
#допиши программу
if searching in trips:
    print('Запрос найден в пожеланиях')
else:
    print('Такого пожелания нет')


subjects = list()
subject = input('Введи предмет (0 - остановить ввод):')
subject = subject.lower()
while subject != '0':
   if subject in subjects:
       print('Этот предмет уже записан')
   else:
       subjects.append(subject)
   subject = input('Введи предмет (0 - остановить ввод):')
   subject = subject.lower()
subjects.sort()
print('Список предметов:', subjects)


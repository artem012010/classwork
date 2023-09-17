while True:
   try:
       children_amount = int(input('Введите число детей'))
       sweets_amount = int(input('Введите количество конфет'))
       break
   except:
       print('Ошибка! Количество должно быть целым числом')
try:
   portion = sweets_amount/children_amount
   print('Каждый ребёнок получит', portion, 'конфет(-ы)')
except:
   print('Ошибка деления! Возможно, пришло 0 детей?')


print('Как называется самая высокая гора мира?')
while True:
    answer = input('1 - Эльбрус, 2 - Мауна-Лоа, 3 - Эверест, 4 - Денали')
    try:
        answer = int(answer)
        break
    except:
        print('Ошибка! Введите номер правильного ответа')
if answer == 3:
    print('Абсолютно верно!')
else:
    print('Нет. Эверест, 8848 метров')


print('Как расшифровывается ВОЗ?')
print('1-Всемирная организация здравоохранения')
print('2-Всероссийская организация защиты')
print('3-Всероссийская особая здравница')
print('4-Владение особого значения')
while True:
   try:
       answer = int(input())
       break
   except:
       print('Ошибка! Введите номер правильного ответа')
if answer == 1:
   print('Абсолютно верно!')
else:
   print('Нет. ВОЗ - это Всемирная организация здравоохранения')


students = ['Смирнов', 'Иванов', 'Васильев', 'Молоткова', 'Алексашкина', 'Гришин']
amount_students = len(students)
students.sort()
i = 1
print('Список класса:')
for student in students:
   print(i, '-', student)
   i += 1
print('Всего учеников:', amount_students)

trips = ['эрмитаж', 'московский зоопарк', 'кремль', 'зоологический музей']
searching = input('Запрос:')
searching = searching.lower()
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

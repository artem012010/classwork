Ответы на задания

Задание 1. «Всё на пять: архив»
1.1. Правильные варианты ответов:


1.2. Правильные варианты ответов:
	

1.4. Дописанная программа:
students = ['Смирнов', 'Иванов', 'Васильев', 'Молоткова', 'Алексашкина', 'Гришин']
amount_students = len(students)
students.sort()
i = 1
print('Список класса:')
for student in students:
   print(i, '-', student)
   i += 1
print('Всего учеников:', amount_students)

1.5. Дописанная программа:
trips = ['эрмитаж', 'московский зоопарк', 'кремль', 'зоологический музей']
searching = input('Запрос:')
searching = searching.lower()
if searching in trips:
   print('Запрос найден в пожеланиях')
else:
   print('Такого пожелания нет')



1.6. Текст программы:
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

1.7. Текст программы:
marks = list()
amount_five = 0
amount_four = 0
amount_three = 0
mark = int(input('Введи оценку (0 - остановить ввод):'))
while mark != 0:
   if mark == 5:
      amount_five += 1
   if mark == 4:
      amount_four += 1
   if mark == 3:
      amount_three += 1
   marks.append(mark)
   mark = int(input('Введи балл (0 - остановить ввод):'))
progress = (amount_five + amount_four + amount_three)/len(marks)*100
print('Список оценок:', marks)
print('Успеваемость:', progress)



Доп задание 1.1. Правильная категоризация:
	


Доп задание 1.2
students = ['Василькова - 5', 'Петров - 4', 'Игнатова - 3', 'Иванова - 4', 'Васильев - 5']
amount_students = len(students)
average_mark = 0
for student in students:
   mark = int(student[len(student)-1]) #оценка - это последний символ любого элемента списка
   average_mark += mark
average_mark = average_mark / len(students)
print('Средний балл:', average_mark)


Доп задание 1.4




Задание 2. «Всё на пять: архив 2»

2.1. Верны следующие варианты ответов:



2.3. Дописанная программа:
marks = input('Введите оценки через пробел:')
marks = marks.split(' ')
print('Анализ набора', marks)
growth = 1 #по умолчанию у всех рост
for i in range(len(marks)-1):
   if marks[i+1] < marks[i]:
       growth = -1
if growth == 1:
   print('Стабильная успеваемость!')
else:
   print('Стабильной успеваемости нет')

2.4. Текст программы для определения вероятности:
marks = input('Введите оценки через пробел:')
marks = marks.split(' ')
amount_five = 0
for mark in marks:
  if mark == '5':
      amount_five += 1
chance = amount_five/len(marks)*100
print('Коэффициент идеальности (%) -', chance)



2.6. Программа-личный кабинет учителя:
def print_students(my_students):
 print('Список класса:')
 i = 1
 for student in my_students:
     print (i, '-', student)
     i += 1


my_students = ['Абрикосов', 'Воробьева', 'Лисицын', 'Олейник', 'Щукина']
print_students(my_students)


student = input('Введите фамилию студента:')
my_students.append(student)
my_students.sort()
print_students(my_students)




Доп задание. 2.1:
student_name = input('Введите фамилию ученика:')
student_marks = input('Введите оценки ученика:')
student_marks = student_marks.split(' ')
student = list()
student.append(student_name)
student.append(student_marks)
print(student)


Доп задание 2.2:

Доп задание 2.3
teacher = list()
teacher_name = input('Фамилия учителя:')
teacher_position = input('Должность:')
students_amount = input('Количество учеников в классах:')
students_amount = students_amount.split(' ')
teacher.append(teacher_name)
teacher.append(teacher_position)
teacher.append(students_amount)
print(teacher)


Дополнительное задание. «Всё на пять: доп задачи»
1.1. Верные варианты ответов:



1.2. Код программы:
from random import randint


students = input('Введите фамилии учеников через пробел:')
students = students.split(' ')
amount = len(students)
numbers = list()
for student in students:
   number = randint(1, amount)
   numbers.append(number)
print('Распределение вариантов контрольной работы')
for i in range(amount):
   print(students[i], '-', numbers[i])


1.3. Код программы:
def get_info():
   student_name = input('Фамилия студента:')
   student_subjects = input('Профильные предметы:')
   student_subjects = student_subjects.replace(',', '')
   student_subjects = student_subjects.split(' ')
   student_subjects.sort()
   student = list()
   student.append(student_name)
   student.append(student_subjects)
   return student


def print_info(student):
   print('Анкета студента')
   print('Фамилия -', student[0])
   print('Профильные предметы:')
   i = 1
   for subject in student[1]:
       print(i, '-', subject)
       i += 1


student1 = get_info()
student2 = get_info()
print_info(student1)
print_info(student2)

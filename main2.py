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




marks = input('Введите оценки через пробел:')
marks = marks.split(' ')
amount_five = 0
for mark in marks:
  if mark == '5':
      amount_five += 1
chance = amount_five/len(marks)*100
print('Коэффициент идеальности (%) -', chance)



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

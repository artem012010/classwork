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

subjects = list()
subject = input('Введи предмет (0 - остановить ввод):').lower()

while subject != '0':
   if subject in subjects:
       print('Этот предмет уже записан')
   else:
       subjects.append(subject)
   subject = input('Введи предмет (0 - остановить ввод):').lower()

subjects.sort()
print('Список предметов:', subjects)


marks = list()
amount = 0
mark = int(input('Введи оценку (0 - остановить ввод):'))
while mark != 0:
   if mark > 2:
      amount += 1
   marks.append(mark)
   mark = int(input('Введи балл (0 - остановить ввод):'))
progress = (amount)/len(marks)*100
print('Список оценок:', marks)
print('Успеваемость:', progress)

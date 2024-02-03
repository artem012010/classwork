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

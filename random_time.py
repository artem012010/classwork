Ответы на задания

Задание 1. «Go Ahead: случайные данные»
1.1. Правильный ответ:
	

1.3. Программа без ошибок:
from random import randint


win_number = 1010
current_number = randint(1000, 3112)
print('Номер лотерейного билета:', current_number)
if current_number == win_number:
   print('Вы выиграли ужин в ресторане!')
else:
   print('Повезёт в другой раз!')

1.4. Полный текст программы:
from random import randint


race1_participants = 0
race2_participants = 0


while input('Выдать номер забега (off - стоп)?') != 'off':
   race_number = randint(1, 2)
   print('Ваш номер', race_number)
   if race_number == 1:
       race1_participants += 1
   else:
       race2_participants += 1
   print('Участников в первом забеге', race1_participants)
   print('Участников во втором забеге', race2_participants)


1.5. Программа:
	from random import randint


group1 = int(input('Число участников сборной 1:'))
group2 = int(input('Число участников сборной 2:'))
swimmer1 = randint(1, group1)
swimmer2 = randint(1, group2)
print('Пловец', swimmer1, '- пловец', swimmer2)

Доп задание 1.1.


Доп задание 1.2
from random import randint
alphabet = 'ABCDEFGH'
line = alphabet[randint(0, 7)]
row = randint(1, 8)
move = line + str(row)
print('Ходить фигурой, стоящей в клетке', move)

Задание 2. «Go Ahead: время»
2.1. Правильный ответ:


2.3.  Исправленная программа:
from time import time


rest = 30
move = ''
begining = time()
while rest > 0 and move != 'off':
   move = input('Ваш ход (off - сдаться):')
   end = time()
   rest = 30 - (end - begining)/60
   print('Осталось', int(rest), 'минут из 30')

2.4. Завершенная программа:
from time import time


stopwatch = input('1 - старт:')
while stopwatch != '0':
   if stopwatch == '1':
       start = time()
   else:
       print('Действие не найдено!')
   stopwatch = input('0 - стоп:')
end = time()
total = int(end-start)
print('Общее время:', total, 'c')

2.5. Программа:
from time import sleep


max_count = int(input('Введите количество секунд:'))
counter = max_count
while counter > 0:
    print(counter)
    counter -= 1
    sleep(1)


Доп задание. 2.1:
	


Доп задание 2.2:
from time import *

answer = input('Удалить с поля? (да/нет)')
if answer == 'да':
   period = int(input('На сколько минут? (2/10)'))
   print('Вы удалены с поля на', period, 'минут(-ы)')
   sleep(period*60)
   print('Возвращайтесь на поле!')

Дополнительное задание. «Go Ahead: доп задания»
1.1. Верные ответы:

 
1.2. Текст программы:
from random import randint
total_teams = int(input('Введите количество команд:'))
name = input('Имя игрока (0 -  завершить):')
while name != '0':
  team_num = randint(1, total_teams)
  print(name + ', номер вашей команды', team_num)
  name = input('Имя игрока (0 -  завершить):')



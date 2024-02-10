Ответы на задания

Задание 1. «Go Ahead: создание модулей»
1.1. Программа модуля:


1.3. Текст модуля для сохранения:
def print_football():
   print('Время игры: два тайма по 45 минут')
   print('Количество игроков: 11 от одной команды')
   print('Цель игры - забить как можно больше мячей в ворота соперника')


def print_hockey():
   print('Время игры: три периода по 20 минут')
   print('Количество игроков: 6 от одной команды')
   print('Цель игры - забросить как можно больше шайб в ворота соперника')


def print_sprint():
   print('Время забега: не ограничено')
   print('Цель - достичь финиша как можно быстрее')
   print('Интересные факты:')
   print('-Старейшая дисциплина лёгкой атлетики, существующая со времён первых Олимпийских игр')
   print('-Абсолютный рекорд (9,63 сек) установлен в 2012 году У. Болтом')

1.4. Текст программы:
import sport_rules
print('Сегодня в программе:\n1-футбол\n2-хоккей\n3-бег на 100 м')
answer = input('Ваш выбор (off - завершить):')
while answer != 'off':
   if answer == '1':
       sport_rules.print_football()
   elif answer == '2':
       sport_rules.print_hockey()
   elif answer == '3':
       sport_rules.print_sprint()
   else:
       print('Вид спорта не найден!')
   answer = input('Ваш выбор (off - завершить):')

1.5 Верное соответствие:
 

1.6. Текст модуля для сохранения:
def get_full_time(experience):
   salary = 20000
   if experience >= 3 and experience < 5:
       k = 1.5
   elif experience >= 5 and experience < 7:
       k = 2
   elif experience >= 7:
       k = 3
   else:
       k = 1
   salary *= k
   return salary


def get_part_time(hours):
   per_hour = 800
   salary = hours*per_hour
   return salary

1.7. Текст программы:
import sport_salary


surname = input('Фамилия тренера:')
job = input('Занятость (1-полная, 2-почасовая):')
if job == '1':
   experience = int(input('Стаж в годах:'))
   salary = sport_salary.get_full_time(experience)
elif job == '2':
   hours = int(input('Отработано часов:'))
   salary = sport_salary.get_part_time(hours)
print(surname, '-', salary)


1.8. Текст модуля:
def get_ticket_price():
   price = 2000
   number = int(input('Номер заказа:'))
   if number % 1000 == 0:
       price *= 0.8
   return price


def get_total_price():
   total = 0
   while input('Купить билет? (off - завершить)') != 'off':
       current_price = get_ticket_price()
       print('Цена за билет:', current_price)
       total += current_price
   print('Итого к оплате:', total)


1.9. Текст программы:
import sale
answer = input('Желаете посетить чемпионат мира по футболу? (да/нет)')
if answer == 'да':
   sale.get_total_price()
else:
   print('Жаль!')


Доп. задание 3. Верные утверждения:


Задание 2. «Проект Автоответчик»
файл 1:

def analyse(phrase):
   phrase = phrase.lower()
   res = phrase.find('расп')
   if res != -1:
       print_schedule()


   res = phrase.find('тренер')
   if res != -1:
       print_trainer_info()


   res1 = phrase.find('оплат')
   res2 = phrase.find('деньг')
   if res1 != -1 or res2 != -1:
       calc_money()


def print_schedule():
   print('Расписание тренировок:')
   print('ПН 15:00 - общая силовая тренировка\nСР 15:00 - бассейн\nПТ 17:00 - бассейн')


def print_trainer_info():
   print('Главный тренер: Борисов Иван Сергеевич, 8800231344')
   print('Тренер по плаванию: Светлова Ирина Олеговна, 88002313234')


def calc_money():
   trainings = int(input('Сколько тренировок вы посетили?'))
   print('К оплате:', trainings*1500)


файл 2:


from analyser import *
request = input('Чем я могу вам помочь?')
while request != 'off':
   analyse(request)
   request = input('Чем я ещё могу вам помочь? (off - завершить)')



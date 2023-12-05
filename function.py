1.2. Программа для клавиатурного тренажёра:
def check_result(score):
   if score >= 100:
       print('Задание пройдено!')


check_result(114)

1.3. Исправленная программа:

def print_label():
   print('-ОТКРЫТИЕ-')
   print('Надо двигаться вперёд, столько классного нас ждёт!')


amount = int(input('Количество футболок:'))
for i in range(amount):
   print_label()

1.4. Завершённая программа:

def student_info(name, course):
   print('Студент', name, 'обучается на курсе', course)


st_name = input('Имя:')
st_course = input('Курс:')
student_info(st_name, st_course)

1.5. Текст программы:

def print_label():
   print('-Золотое пёрышко-')
   print('Имя: ____')
   print('Школа: ____')


amount = int(input('Число учеников:'))
for i in range(amount):
   print_label()
print('Готово! Заберите бейджики.')

Доп. задание 1.1 Правильные ответы:



Доп. задание 1.2 Текст программы:

def set_status(score):
   print('Ваша скидка:')
   if score > 0 and score < 50:
       print('Скидка 10%')
   elif score >= 50 and score < 100:
       print('Скидка 15%')
   elif score >= 100:
       print('Скидка 20%')


score = int(input('Набрано баллов:'))
set_status(score)


Задание 2. «Центр: автоматизация 2»

2.1. Правильные варианты ответов:
	



2.3.  Программа после исправлений:

def check_test(score):
   if score >= 80:
      return True
   else:
       return False
amount = int(input('Введите число участников:'))
for i in range(amount):
   name = input('Введите имя:')
   score = int(input('Введите баллы за тест:'))
   res = check_test(score)
   print('Допуск:', res)

2.4.  Дописанная программа:

def get_course(wish):
   if wish.find('спорт') != -1:
       course = 'волейбол'
   elif wish.find('наука') != -1:
       course = 'астрономия'
   elif wish.find('комиксы') != -1:
       course = 'скетчинг'
   else:
       course = 'история Древнего Рима'
   return course


amount = int(input('Число учеников:'))
for i in range(amount):
   wish = input('Введите предпочтение:')
   course = get_course(wish)
   print('Рекомендация:', course)
   if course == 'астрономия':
       print('Будьте внимательны! Занятия проходят ночью!')

2.5. Написанная программа:

def is_camp(grade):
   if grade > 50:
       return True
   else:
       return False
amount = int(input('Число учеников:'))
for i in range(amount):
   grade = int(input('Введите балл:'))
   res = is_camp(grade)
   print('Допуск:', res)
   if res == False:
       print('Займитесь чтением! Отличные книги: Три толстяка, Дон Кихот и Робинзон Крузо')

Доп. задание 2.1. Правильные ответы:



Доп. задание 2.2. Текст программы:


def is_ok(score):
   if score < 100:
       return False
   else:
       return True
score = int(input('Введите количество баллов:'))
print('Доступен ли мерч:', is_ok(score))


Дополнительное задание «Центр: доп. задания»
1.1. Верные ответы:
	


1.2. Программа для клавиатурного тренажёра:
def is_allowed(grade):
   if grade <= 3:
       return False
   else:
       return True
res = is_allowed(4)


1.3. Исправленная программа:


def buy_ticket(price):
   ans = input('Желаете оформить страховку на время перелёта?')
   if ans == 'да':
      price += 500
   ans = input('Желаете приобрести питание на борту?')
   if ans == 'да':
      price += 700


   return price
price = 2000
final_price = buy_ticket(price)
print('Стоимость билета с учётом услуг:', final_price)


1.4. Код программы:
def print_paper(st_name, st_class):
   print(
       'Объявляется благодарность ученику(-це)', st_name, st_class,
       'класса. Учительский коллектив центра УСПЕХ искренне поздравляет с окончанием учебного года и желает дальнейших успехов в учёбе.')


n = int(input('Число отличников:'))
for i in range(n):
   st_name = input('Введите имя:')
   st_class = input('Введите класс:')
   print_paper(st_name, st_class)

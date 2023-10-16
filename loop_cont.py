Задание 1. «Друг вокруг: авторизация»

1.4. Программа :
for i in range(3):
   wish = input('Введите предпочтение:')
   print('Предпочтение учтено')
print('Система рекомендаций настроена!')

1.5. Программа после исправления ошибок:
total = 0
count = int(input('Количество оценок:'))
for i in range(count):
    mark = int(input('Оценка:')) 
    total += mark
print('Среднее:', total/count)


1.6. Завершенная программа:
count = int(input('Число участников:'))
for i in range(count):
    name = input('Введите имя:')
    print('Добро пожаловать,', name)
print('Групповой чат создан!')

1.7. Программа:
password = input('Введите логин:')
wrong = '=?*^$№@_'
for symbol in password:
    if symbol in wrong:
        print('Запрещённый символ:', symbol)

Доп задание 1.1.


Доп задание 1.2
password = input('Введите пароль:')
password = password.lower()
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for symbol in password:
    print(alphabet.find(symbol) + 1)

Доп задание 1.3
count = int(input('Число пользователей:'))
for i in range(count):
    login = input('Логин:')
    age = int(input('Возраст:'))
    if age >= 14:
        print('Аккаунт создан:', login)
    else:
        print('Ошибка: возраст меньше 14 лет.')



Задание 2. «Друг вокруг: личный кабинет»

2.3.  Программа после исправлений:
number = input('Введите 1 - рекомендация, off - завершить')
while number != 'off':
    if number == '1':
        preference = input('Ваше настроение:')
        if preference == 'весёлое':
            print('Мультфильм Шрек')
        else: 
            print('Мультфильм Алладин')
    number = input('Введите 1 - рекомендация, off - завершить')

2.4. Завершенная программа:
for i in range(1, 4):
    if input('Введите название игры:') == 'FIFA':
        print('Поздравляем! Вы угадали с попытки №', i)
        break

2.5. Программа:
number = input('Введите 1 - рекомендация, 2 - розыгрыш, off - завершить')
while number != 'off':
   if number == '1':
       preference = input('Введите предпочтение:')
       if preference == 'спорт':
           print('Подкаст Убойный спорт')
       else:
           print('Новый альбом Канье Уэста')
   elif number == '2':
       for i in range(1, 4):
           if input('Введите название группы') == 'Queen':
               print('Вы выиграли билет на концерт!')
               break
   number = input('Введите 1 - рекомендация, 2 - розыгрыш, off - завершить')


Доп задание. 2.1:
message = 'ППррииввеетт!!  ККаакк  ддееллаа??  ССееггоодднняя  ттааккааяя  ххоорроошшааяя  ппооггооддаа,,  ммоожжеетт  ппооггуулляяеемм??'


result = ''
for i in range(0, len(message), 2):
    result += message[i]


print(result)


Доп задание 2.2:
vowels = 'аеёиоуыэюя'
consonants = 'бвгджзйклмнпрстфхцчшщъь'


password = input('Введите пароль:')
password = password.lower()
result = ''
for symbol in password:
    if symbol in vowels:
        result += '0'
    elif symbol in consonants:
        result += '1'
print(result)


Дополнительное задание. «Друг вокруг: доп задания»

1.2. Завершенная программа:
for i in range(3):
  login = input('Логин:')
  password = input('Пароль:')
  if login == 'admin' and password == 'trGd3j':
      print('Авторизация пройдена с попытки', i+1)
      break
if login != 'admin' or password != 'trGd3j':
   print('Доступ запрещён')


1.3. Код программы:
hero = input('Введите персонажа (off-завершить):')
while hero != 'off':
   if hero == 'Питер Паркер':
       print('Человек-паук')
   elif hero == 'Аслан':
       print('Хроники Нарнии')
   elif hero == 'Джек Воробей':
       print('Пираты Карибского моря')
   elif hero == 'Мастер Шифу':
       print('Кунг-фу панда')
   elif hero == 'Фиона':
       print('Шрек')
   else:
       print('Я пока не знаю такого персонажа:(')
   hero = input('Введите персонажа (off-завершить):')


1.4. Код программы:
tel = input('Введите номер телефона:')
permitted = '0123456789+'


for symbol in tel:
    if symbol not in permitted:
        print('Неправильный номер телефона!')
        break

Ответы на задания

Задание 1. «Библиотека: каталог»
1.1. Правильные варианты ответов:


1.4. Дописанная программа:
books = {
  'Кинг': 'Оно',
  'Лондон': 'Белый клык',
  'Кэрролл': 'Алиса в стране чудес',
  'Линдгрен': 'Карлсон, который живёт на крыше'}


books['Дефо'] = 'Приключения Робинзона Крузо'
books['Дюма'] = 'Граф Монте-Кристо'
del books['Кинг']


if 'Дефо' in books and 'Дюма' in books:
   print('База обновлена!')
if ('Кинг' in books) == False:
   print('Предпочтения обновлены')



1.5. Текст программы:
authors = {
   'Пушкин' : 'Русский поэт, драматург и прозаик. Один из самых авторитетных литературных деятелей первой трети XIX века',
   'Толстой' : 'Один из наиболее известных русских писателей и мыслителей, один из величайших писателей-романистов мира',
   'Бунин' : 'Русский писатель, поэт и переводчик, лауреат Нобелевской премии по литературе 1933 года'}
surname = input('Фамилия автора:')
if surname in authors:
   print('Биография:', authors[surname])
else:
   answer = input('Автор не найден. Добавить?')
   answer = answer.lower()
   if answer == 'да':
       biography = input('Его биография:')
       authors[surname] = biography
       print(authors)
   else:
       print('Ответ получен')

1.6. Текст программы:
student_card = {'номер': '324', 'фамилия': 'Иванов'}
print('Добро пожаловать!', student_card)
answer = int(input('Личный кабинет: 1 - взять, 2 - вернуть, 3 - домой'))
while answer != 3:
   if answer == 1:
       title = input('Введите название:')
       student_card['долг'] = title
       print('Карточка читателя:', student_card)
   if answer == 2:
       if 'долг' in student_card:
           del student_card['долг']
       print('Карточка читателя:', student_card)
   answer = int(input('Ваше действие: 1 - взять, 2 - вернуть, 3 - домой'))
print('Ждём вас:', student_card)

Доп задание 1.1. Правильная категоризация::


Доп задание 1.2 Текст программы:
readers = {214: 'Иванов, 7а', 122: 'Котов, 6б', 59: 'Васина, 11а', 368: 'Петренко, 2г'}
number = input('Добро пожаловать! Ваш читательский билет:')
while True:
   try:
       number = int(number)
       break
   except:
       number = input('Введите номер числом:')
if number in readers:
   print('Здравствуйте, читатель(-ница)', readers[number])
else:
   print('Данный читательский билет не найден!')

Доп задание 1.3. Текст программы:
class Reader:
   def __init__(self, Surname, Grade, Books):
       self.Surname = Surname
       self.Grade = Grade
       self.Books = Books
   def print_data(self):
       print(self.Surname, '-', self.Grade, '-', self.Books)


print('Создание читательской учётной записи')
surname = input('Введите фамилию:')
grade = input('Введите класс:')


Student_Reader = Reader(surname, grade, [])
answer = input('Хотите взять книгу? (да/нет)')
if answer == 'да':
   book = input('Название книги (off - завершить):')
   while book != 'off':
       Student_Reader.Books.append(book)
       book = input('Название книги (off - завершить):')
Student_Reader.print_data()


Доп задание 1.4. Правильные ответы:



Задание 2. «Всё на пять: проверка 2»
2.1. Заполненные пропуски:



2.3. Дописанная программа:
my_shelf = dict()
author = input('Введите автора:')
book = input('Введите книгу (s - стоп):')
books = list()
while book != 's':
   books.append(book)
   book = input('Введите книгу (s - стоп):')
my_shelf[author] = books
print(my_shelf)

2.4. Текст программы с книжной полкой:
my_shelf = dict()
author = input('Введите автора (q - завершить):')
while author != 'q':
   books = list()
   book = input('Введите книгу (s - стоп):')
   while book != 's':
       books.append(book)
       book = input('Введите книгу (s - стоп):')
   my_shelf[author] = books
   author = input('Введите автора (q - завершить):')


for author in my_shelf:
   print(author, '-', my_shelf[author])

2.5. Текст программы:
from random import randint
authors = {
   'Пушкин': ['Сказки', 'Дубровский', 'Руслан и Людмила'],
   'Бианки': ['Мышонок Пик', 'Лесная газета', 'Чей нос лучше'],
   'Зощенко': ['Рассказы', 'Голубая книга', 'Лёля и Минька'],
   'Лондон': ['Белый клык', 'Зов предков', 'Мартин Иден'],
   'Заболоцкий': ['Стихи', 'Некрасивая девочка', 'Как мыши с котом воевали'],
   'Кристи': ['Десять негритят', 'Убийство в Восточном экспрессе', 'Труп в библиотеке'],
   'Распутин': ['Уроки французского', 'Дочь Ивана, мать Ивана', 'Рудольфио'],
   'Тургенев': ['Бежин луг', 'Хорь и Калиныч', 'Первая любовь'],
   'Толстой': ['Кавказский пленник', 'Детство', 'Филипок'],
   'Астафьев': ['Конь с розовой гривой', 'Царь-рыба', 'Людочка']
}


author = input('Испытайте удачу! Введите автора:')
if author in authors:
   number = randint(0, 2)
   print('Рекомендованная книга:', authors[author][number])
else:
   print('Автор не найден!')
Доп задание. 2.1:

Доп задание 2.2:
souvenirs = {
   'футболки': ['I love Pushkin!', 'Это время — трудновато для пера', 'Здоровы и нормальны только заурядные люди'],
   'браслеты': ['Читайте, завидуйте, я - гражданин!', 'Гой ты, Русь моя родная!'],
   'сумки': ['С портретом Чехова', 'С цитатой Гоголя', 'С пером']
}
print('Ассортимент магазина:')
for category in souvenirs:
   print(category)
   for product in souvenirs[category]:
       print('-', product)
answer = int(input('Что желаете? 1-футболка, 2-браслет, 3-сумка'))
if answer == 1:
   print('К оплате: 1500 рублей')
elif answer == 2:
   print('К оплате: 300 рублей')
elif answer == 3:
   print('К оплате: 600 рублей')
else:
   print('Некорректный номер')




Дополнительное задание. «Библиотека: доп задачи»
1.1. Верные варианты ответов:
	
1.2. Код программы:
readers = {
   'akuznecov': ['Старуха Изергиль', 'Задачник по математике']
}
login = input('Введите логин')
if login in readers:
   print('Авторизация успешна! Ваши книги')
   print(readers['akuznecov'])
else:
   answer = input('Логин не найден. Добавить? (да/нет)')
   if answer == 'да':
       books = list()
       book = input('Логин добавлен. Введите желаемую книгу (s - stop)')
       while book != 's':
           books.append(book)
           book = input('Введите желаемую книгу (s - stop)')
       readers[login] = books


       print('Наши читатели:')
       for reader in readers:
           print(reader, '-', readers[reader])

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


my_shelf = dict()
author = input('Введите автора:')
book = input('Введите книгу (s - стоп):')
books = list()
while book != 's':
   books.append(book)
   book = input('Введите книгу (s - стоп):')
my_shelf[author] = books
print(my_shelf)


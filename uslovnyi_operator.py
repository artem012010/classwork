1.5. Программа после исправления ошибок:
login = 'ivanova.ekaterina'
password = input(login + ', введите пароль для входа в личный кабинет:')
ok = password == 'sweetstore111'
print('Авторизация:', ok)

1.6. Программа после исправления ошибок:
category = input('Введите вид кондитерской продукции:')
taste = input('Введите вкус:')
category = category.lower()
taste = taste.lower()
is_top = category == 'торт' and taste == 'шоколадный'
print('Задан самый популярный запрос:', is_top)

1.7. Текст программы для назначения товаров по акции:
category = input('Введите вид кондитерской продукции:')
price = int(input('Введите допустимую для вас цену:'))
category = category.lower()
is_sale = category == 'пирожные' and price <= 500
print('Предлагать продукцию по акции:', is_sale)

1.8. Текст программы для назначения диетических товаров:
wish = input('Пожелание:')
wish = wish.lower()
suggest = wish == 'без сахара' or wish == '0% жирности' or wish == 'без глютена'
print('Предлагать диетические товары:', suggest)
	
	Возможно альтернативное решение с функцией str.find().

Доп задание 1.1.


Доп задание 1.2
product = input('Вид продукта:')
taste = input('Начинка:')
product = product.lower()
taste = taste.lower()
suggest = product == 'печенье' and taste == 'крем' or product == 'печенье' and taste == 'джем'
print('Заказано популярное печенье с начинкой:', suggest)


Доп задание 1.3
allergic = input('Есть аллергия:')
allergy = input('Аллергия на:')
allergic = allergic.lower()
allergy = allergy.lower()
is_allergic = allergic == 'да' or allergic == 'есть'
suggestion = allergy != 'молоко' and allergy != 'глютен'
print('Наличие аллергии:', is_allergic)
print('Предлагать ватрушки с творогом:', suggestion)


Задание 2. «Кондитерская: рекомендации»

2.1. Верны следующие варианты ответов:


2.4. Программа после исправления ошибок:
answer = input('Вы первый раз в Сладких историях?')
answer = answer.lower()
if answer == 'да':
   print('Скидка 40% для новичков. Промокод NEW')
else:
   print('Торты со скидкой 10%. Промокод CAKE')

2.5. Программа после исправления ошибок:
max_price = int(input('Какую сумму вы готовы потратить на сладости?'))
if max_price < 500:
   print('Попробуйте пирожные со сгущенкой!')
if max_price >= 500 and max_price <= 1000:
   print('Побалуйте себя тортиком Секрет!')
if max_price > 1000:
   print('Угоститесь шоколадным фонданом с голубикой!')


2.6. Программа для рекомендации десерта по весу
height = int(input('Введите ваш рост:'))
weight = int(input('Введите ваш вес:'))
difference = height - weight
if difference > 100:
   print('Ваш вес в норме. Может, по круассану с кремом?')
else:
   print('Попробуйте ягодный мусс. Он не причинит вред фигуре!')


2.7. Программа для рекомендации десерта по возрасту:
age = int(input('Введите возраст:'))
if age < 30:
   print('Люди вашего возраста часто берут мороженое с фисташками')
else:
   print('Люди вашего возраста часто берут тёмный шоколад')
print('Переходите к покупкам!')




Доп задание. 2.1:

Доп задание 2.2:
weight = int(input('Введите желаемый вес десерта в килограммах:'))
if weight < 2:
   print('Попробуйте корзиночки со сливками')
if weight >= 2 and weight <= 3:
   print('Как насчёт ассорти мини-тортиков?')
if weight > 3:
   print('Рекомендуем многоярусный торт')
print('Переходите к покупкам!')


Доп задание 2.4:



Дополнительное задание. «Кондитерская: доп задание»
1.1. Верные варианты ответов:

1.3. Код программы без ошибок:
wish = input('Введите пожелание:')
if wish == 'крем':
   print('Попробуйте заварные пирожные')
if wish == 'изюм':
   print('Попробуйте фирменные кексы')
if wish != 'крем' and wish != 'изюм':
   print('Попробуйте рогалики с маком')


1.4. Код программы:
weight = int(input('Введите вес торта в граммах:'))
taste = input('Введите начинку:')
if weight <= 2500:
   price = 3000
else:
   price = 5000
if taste == 'фрукты':
   price = price + 1000
	else:
   price =  price + 500
print('Примерная цена торта:', price)

import pandas as pd
df = pd.read_csv('GoogleApps.csv')


# 1 Сколько всего приложений с категорией ('Category') 'BUSINESS'?
temp = df['Category'].value_counts()
print(temp['BUSINESS'])


# 2 Чему равно соотношение количества приложений для подростков ('Teen') и для детей старше 10 ('Everyone 10+')?
# Ответ запиши с точностью до сотых.
temp = df['Content Rating'].value_counts()
print('Соотношение:', temp['Teen'] / temp['Everyone 10+'])


# 3.1 Чему равен средний рейтинг ('Rating') платных ('Paid') приложений?
# Ответ запиши с точностью до сотых.
temp = df.groupby(by = 'Type')['Rating'].mean()
print(temp['Paid'])


# 3.2 На сколько средний рейтинг ('Rating') бесплатных ('Free') приложений меньше среднего рейтинга платных ('Paid')?
# Ответ запиши с точностью до сотых.
print(temp['Paid'] - temp['Free'])


# 4 Чему равен минимальный и максимальный размер ('Size') приложений в категории ('Category') 'COMICS'?
# Запиши ответы с точностью до сотых.
temp = df.groupby(by = 'Category')['Size'].agg(['min', 'max'])


# Бонус 1. Сколько приложений с рейтингом ('Rating') строго больше 4.5 в категории ('Category') 'FINANCE'?
temp = df[df['Rating'] > 4.5]['Category'].value_counts()
print(temp['FINANCE'])


# Бонус 2. Чему равно соотношение бесплатных ('Free') и платных ('Paid') игр с рейтингом ('Rating') больше 4.9?
temp = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]['Type'].value_counts()
print(temp['Free'] / temp['Paid'])








import pandas as pd
df = pd.read_csv('GoogleApps.csv')


# 1 Выведи на экран минимальный, средний и максимальный рейтинг ('Rating') платных и бесплатных приложений ('Type') с точностью до десятых.
print(df.groupby(by = 'Type')['Rating'].agg(['min', 'mean', 'max']))


# 2 Выведи на экран минимальную, медианную (median) и максимальную цену ('Price') платных приложений (Type == 'Paid') для # разных целевых аудиторий ('Content Rating')
print(df[df['Type'] == 'Paid'].groupby(by = 'Content Rating')['Price'].agg(['min', 'median', 'max']))


# 3 Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом
# посчитай максимальное количество отзывов ('Reviews') в каждой группе.
# Сравни результаты для категорий 'EDUCATION', 'FAMILY' и 'GAME':
# В какой возрастной группе больше всего отзывов получило приложение из категории 'EDUCATION'? 'FAMILY'? 'GAME'?


# Подсказка: ты можешь выбрать из DataFrame несколько столбцов одновременно с помощью такого синтаксиса:
# df[[<столбец 1>, <столбец 2>, <столбец 3>]]
temp = df.pivot_table(index = 'Content Rating', columns = 'Category', values = 'Reviews', aggfunc = 'max')
#print(temp[['EDUCATION', 'FAMILY', 'GAME']])


# 4 Сгруппируй платные (Type == 'Paid') приложения по категории ('Category') и целевой аудитории ('Content Rating')
# Посчитай среднее количество отзывов ('Reviews') в каждой группе
# Обрати внимание, что в некоторых ячейках полученной таблицы отражается не число, а значение "NaN" - Not a Number
# Эта запись означает, что в данной группе нет ни одного приложения.
# Выбери названия категорий, в которых есть платные приложения для всех возрастных групп и расположи их в алфавитном порядке.
#print(df[df['Type'] == 'Paid'].pivot_table(columns = 'Content Rating', index = 'Category', values = 'Reviews', aggfunc = 'mean'))


# Бонусная задача. Найди категории бесплатных (Type == 'Free') приложений,
# в которых приложения разработаны не для всех возрастных групп ('Content Rating')
#print(df[df['Type'] == 'Free'].pivot_table(index = 'Category', columns = 'Content Rating', values = 'Reviews', aggfunc = 'mean'))

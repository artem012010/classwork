months = 'январь февраль март апрель май июнь июль август сентябрь октябрь ноябрь декабрь'.split()
sales = input('Введите данные о доходах с января по декабрь').split()
sales = list(map(int, sales))
growth = []
fall = []
for i in range(1, len(sales)):
    if sales[i] > sales[i-1]:
        growth.append(months[i])
    if sales[i] < sales[i-1]:
        fall.append(months[i])
print('Месяцы роста доходов:', growth)
print('Месяцы снижения доходов:', fall)



data = dict() 
while input('Желаете посетить урок программирования (да/нет)?').lower() == 'да':
    topic = input('Введите тему урока')
    if topic in data:
        data[topic] += 1 
    else:
        data[topic] = 1 


total_lessons = 0
for lesson in list(data.values()):
    total_lessons += lesson
total_topics = len(data)

print('Общее количество уроков:', total_lessons)
print('Рассмотрено тем:', total_topics)

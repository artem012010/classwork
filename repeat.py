who = input('Введите название своего стартапа')
day = input('Введите дату основания стартапа')
year = int(input('Введите год основания стартапа'))
print('Поприветствуйте', who, '- новый перспективный IT стартап.') 
print('Компания', who, 'была основана', day, year, 'года.')



rur = int(input('Введите сумму в рублях'))
usd = float(input('Введите курс доллара'))
result = round(rur/usd, 2)
print('Результат конвертации:', result)



if input('У вас есть идея собственного продукта (да/нет)?').lower() == 'да':
    if input('Вы заинтересованы в получении инвестиций (да/нет)?').lower() == 'нет':
        print('Рекомендуем вам подать документы в бизнес-школу.')
    else:
        print('У вас есть все шансы попасть в бизнес-акселератор!')
else:
    print('Спасибо, что приняли участие в опросе!')




balance = int(input('Введите текущий баланс карты'))
while balance > 0 and input('Хотите сделать покупку (да/нет)?') == 'да':
    price = int(input('Введите цену'))
    if balance - price < 0:
        print('Недостаточно средств!')
    else:
        balance -= price
        print('Сумма', price, 'руб. списана со счёта.')
print('Доступная сумма:', balance, 'руб.')



start = int(input("Год начала сотрудничества с фондом"))
end = int(input("Год окончания сотрудничества с фондом"))
for year in range(start, end+1):
    if year%2 == 0:
        print(year, "год - серия конференций и круглых столов с экспертами.")
    else:
        print(year, "год - международный конкурс 'Стартап года'.")




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



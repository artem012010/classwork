while True:
   try:
       children_amount = int(input('Введите число детей'))
       sweets_amount = int(input('Введите количество конфет'))
       break
   except:
       print('Ошибка! Количество должно быть целым числом')
try:
   portion = sweets_amount/children_amount
   print('Каждый ребёнок получит', portion, 'конфет(-ы)')
except:
   print('Ошибка деления! Возможно, пришло 0 детей?')


print('Как называется самая высокая гора мира?')
while True:
    answer = input('1 - Эльбрус, 2 - Мауна-Лоа, 3 - Эверест, 4 - Денали')
    try:
        answer = int(answer)
        break
    except:
        print('Ошибка! Введите номер правильного ответа')
if answer == 3:
    print('Абсолютно верно!')
else:
    print('Нет. Эверест, 8848 метров')





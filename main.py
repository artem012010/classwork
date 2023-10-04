promo = input('Введите промокод:')
while promo != 'life' and promo != 'health':
    promo = input('Этот промокод недействителен. Попробуйте снова:')
print('Промокод принят.')


while input('Введите ваш отзыв:') != 'off':
    print('Спасибо, ваш отзыв принят!')


price = int(input('Стоимость товара (0 - покупок больше нет):'))
cost = price
while price != 0:
    price = int(input('Стоимость товара (0 - покупок больше нет):'))
    cost += price           
print('Стоимость всех покупок: ' + str(cost))




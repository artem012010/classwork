class Price_list():
   def __init__ (self,name):
       self.name = name
       self.pricelist = dict()
   def add_price(self, **kwargs):
       for key in kwargs:
           self.pricelist[key] = kwargs[key]
   def order(self, **kwargs):
       sum = 0
       for key in kwargs:
           if key in self.pricelist:
               sum += self.pricelist[key]  * kwargs[key] 
       return sum

my_offer = Price_list('Инстаграм')
my_offer.add_price(management = 1000, content_plan = 850, style = 500, stories = 100, post = 300)
while input('Хотите сделать заказ? (1 - да, 0 - нет)') != '0':
    operation = input('Хотите заказать управление аккаунтами (1) или публикации (2)?')
    if operation == '1':
        management = int(input('Сколько новых аккаунтов хотите добавить?')) 
        content_plan = int(input('Для скольких из них будем делать контент-план?')) 
        style = int(input('Для скольких из них будем разрабатывать стиль?')) 
        price = my_offer.order(management = management, content_plan = content_plan, style = style)
    else:
        stories = int(input('Сколько сториз хотите заказать?'))
        post = int(input('Сколько постов хотите заказать?'))
        price = my_offer.order(stories = stories, post = post)
    print(f'Стоимость услуг: {price} руб.')

print('Спасибо за сотрудничество! Хорошего дня!')

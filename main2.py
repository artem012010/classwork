def print_info(**kwargs):
   for key in kwargs:
       print('Услуга –', key, ', цена –', kwargs[key])
print_info(stories = 100, management = 1000)



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
               sum += self.pricelist[key] * kwargs[key]
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




def count_services(**kwargs):
    total = 0
    categories = 0
    for category in kwargs:
        if kwargs[category] > 0:
            total += kwargs[category]
            categories += 1
    return total, categories



from count_services import count_services


service = input('Для какого сервиса вы хотите заказать услуги (1 - Инстаграм, 2 - YouTube)?')
if service == '1':
    plan = int(input('Введите количество аккаунтов для создания контент-плана'))
    stories = int(input('Введите количество сториз'))
    posts = int(input('Введите количество постов'))
    total, categories = count_services(plan = plan, stories = stories, posts = posts)
else:
    cover = int(input('Введите количество роликов, для которых нужны обложки'))
    editing = int(input('Введите количество роликов, для которых нужен монтаж'))
    total, categories = count_services(cover = cover, editing = editing)


print(f'Услуг: {total}, категорий: {categories}.')
print('Наши специалисты уже начали работу!')



class Land():
   def __init__(self, length, width):
       self.length = length
       self.width = width
   def print_info(self):
       print(f'Длина участка: {self.length}, ширина: {self.width}.')
   def calc_perimeter(self):
       self.perimeter = (self.length + self.width) * 2
       return self.perimeter
   def calc_area(self):
       self.area = self.length * self.width
       return self.area
 
a = int(input('Введите длину:'))
b = int(input('Введите ширину:'))
land_plot = Land(a, b)
land_plot.print_info()
print('Периметр участка:', land_plot.calc_perimeter())
print('Площадь участка:', land_plot.calc_area())


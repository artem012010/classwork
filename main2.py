def print_info(**kwargs):
   for key in kwargs:
       print('Услуга –', key, ', цена –', kwargs[key])
print_info(stories = 100, management = 1000)

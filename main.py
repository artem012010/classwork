class Converter():
   def __init__(self, usd):
       self.usd = usd
 
   def rub_to_usd(self, rub_value):
       usd_value = rub_value/self.usd
       print(round(usd_value, 2))
 
   def usd_to_rub(self, usd_value):
       rub_value = usd_value*self.usd
       print(round(rub_value, 2))
 
a = int(input('Введите курс доллара'))
b = int(input('Введите сумму для обмена'))
conv = Converter(a)
option = int(input('1 - доллары в рубли / 2 - рубли в доллары'))
if option == 1:
   conv.usd_to_rub(b)
else:
   conv.rub_to_usd(b)

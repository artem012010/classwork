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



class Accounting():
    def __init__(self, account):
        self.account = account
    def pay_bill(self, amount):
        if self.account - amount >= 0:
            self.account -= amount
            print(f'Списано {amount} руб. Остаток на счету: {self.account} руб.')
        else:
            print('Недостаточно средств для выполнения операции.')
    def get_money(self, amount):
        self.account += amount
        print(f'Зачислено {amount} руб. Остаток на счету: {self.account} руб.')

amount = int(input('Введите данные о сумме на счету'))
office = Accounting(amount)
while input('Хотите выполнить операцию? (1 - да, 2 - нет)') == '1':
    code = input('Введите код операции (1 - зачисление, 2 - списание)')
    amount = int(input('Введите сумму'))
    if code == '1':
        office.get_money(amount)
    else:
        office.pay_bill(amount)
print('Спасибо за работу! Хорошего вечера!')

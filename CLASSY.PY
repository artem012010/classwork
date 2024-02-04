class My_success():
    def __init__(self,value):
        self.value_of_success = value
    def check_success(self):
        if self.value_of_success >= 4.0:
            return 'Запуск стартапа прошел успешно'
        elif self.value_of_success < 4.0 and self.value_of_success >= 3.0:
            return 'Запуск стартапа прошел неплохо'
        return 'Проект нуждается в доработке'
rate = float(input('Рейтинг приложения'))
object = My_success(rate)
print(object.check_success())

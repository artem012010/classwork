def otvet(zapros):
    zapros = zapros
    if zapros.find('трени') != -1:
        raspisanie()

def raspisanie():
    print('Плавание вт\чт 20:00')
    print('Футбол сб\вс 16:00')

print('Вас приветствует спортивный центр ЗЕВС')
zapros = input('Что бы вы хотели узнать?')
while zapros != 'выйти':
    otvet(zapros)
    zapros = input('Еще что нибудь (выйти - завершение)?')


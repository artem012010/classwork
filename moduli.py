from time import time

while True:
    vremya = input('1 - НАЧАТЬ 0 - ЗАКОНЧИТЬ')
    if vremya == '1':
        start = time()
    if vremya == '0':
        end = time()
        break

print('Прошло', round(end - start,2),'c')


from time import sleep

max_count = int(input('Введите количество секунд:')) 
while max_count >= 0:
    print('До конца света осталось:',max_count, 'c')
    max_count -= 1 
    sleep(1)

print('BOOM')

from time import time

while True:
    vremya = input('1 - НАЧАТЬ 0 - ЗАКОНЧИТЬ')
    if vremya == '1':
        start = time()
    if vremya == '0':
        end = time()
        break

print('Прошло', round(end - start,2),'c')

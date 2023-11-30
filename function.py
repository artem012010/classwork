def five():
    mark = int(input('Оценка (0-завершить):'))
    count = 0
    while mark != 0:
        if mark == 5:
            count += 1
        mark = int(input('Оценка (0-завершить):'))
    return count

def set_discount():
    a = five()
    if a >= 4 and a <= 5:
        return 10
    elif a > 5:
        return 15
    else:
        return 0

print('Скидка на билеты в театр (%):', set_discount())

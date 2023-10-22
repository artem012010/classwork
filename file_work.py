#напиши здесь свою программу
with open('quotes.txt', "r", encoding = "UTF-8") as file:
    for line in file:
        print(line)

author = input("Кто написал эти строки? ")
with open('quotes.txt', "a",  encoding = "UTF-8") as file:
    file.write( "(" + author + ")" + "\n")

while True:
    answer = input("Хотите добавить ещё одну цитату? (да/нет)")
    answer = answer.lower()
    if answer == "да":
        quote = input("Введите цитату: ")
        author = input("Введите автора: ")
        file = open("quotes.txt", "a",  encoding = "UTF-8")
        file.write(quote+"\n"+"("+author+")"+"\n")
        file.close()
    else:
        break

with open('quotes.txt', "r", encoding = "UTF-8") as file:
    for line in file:
        print(line)








#напиши здесь свою программу
import time

class Pupil:
    def __init__(self, Surname, Name, Mark):
        self.Surname = Surname
        self.Name = Name
        self.Mark = Mark

pupils = []

def print_class(pupils):
    for pupil in pupils:
        print(pupil.Surname, pupil.Name, "-", pupil.Mark)
    print("\n")

def print_five(pupils):
    print("Отличники: ")
    for pupil in pupils:
        if pupil.Mark == 5:
            print(pupil.Surname)
    print("\n")

def find_average(pupils):
    average = 0
    for pupil in pupils:
        average += pupil.Mark
    average /= len(pupils)
    print("Средняя оценка класса:", average)

start_time = time.time()
with open("pupils_large.txt", "r", encoding = "utf-8") as file:
    for line in file:
        data = line.split(" ")
        pupil = Pupil(data[0], data[1], int(data[2]))
        pupils.append(pupil)

print_five(pupils)
find_average(pupils)
print("Время выполнения: ", (time.time()-start_time), "секунд")

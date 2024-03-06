with open('quotes.txt', "r", encoding = "UTF-8") as file:
    for line in file:
        print(line)

author = input("Кто написал эти строки? ")
with open('quotes.txt', "a",  encoding = "UTF-8") as file:
    file.write("Автор:"+author+"\n")

while True:
    answer = input("Хотите добавить ещё одну цитату? (да/нет)").lower()
    if answer == "да":
        quote = input("Введите цитату: ")
        author = input("Введите автора: ")
        file = open("quotes.txt", "a",  encoding = "UTF-8")
        file.write(quote+"\n"+"("+author+")"+"\n")
        file.close()
    else:
        break


def log(name, phone, comment):
    with open('phone_book.csv', 'a') as file:
        file.write("{};{};{}\n".format(name, phone, comment))
    print("Абонент {} с номером {} ({}) добавлен".format(name, phone, comment))

def view(what):
    if what == "all":
        with open('phone_book.csv', 'r') as file:  # , encoding="utf-8"
            # lines = file.read()
            for line in file:
                array = list(line.split(';'))
                print("Name: {}, phone: {} - {}" .format(array[0], array[1], array[2]))

def save_to_txt(f_name):
    with open('phone_book.csv', 'r') as file:
        phone_book = file.read()
        phone_book = phone_book.replace(';', ' ')

    with open(f_name + ".txt", 'w') as new_file:
        new_file.write(phone_book)
        print("Данные сохранены в файл {}.txt.".format(f_name))

def save_to_csv(f_name):
    with open('phone_book.csv', 'r') as file:
        phone_book = file.read()
    with open(f_name + ".csv", 'w') as new_file:
        new_file.write(phone_book)
        print("Данные сохранены в файл {}.csv.".format(f_name))
#
# def save_to_html(f_name):
#



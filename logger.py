
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

# def save_to_txt(format):



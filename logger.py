
def log(name, phone, comment):
    with open('phone_book.csv', 'a') as file:
        file.write("{};{};{}\n".format(name, phone, comment))
    print("Абонент {} с номером {} ({}) добавлен".format(name, phone, comment))

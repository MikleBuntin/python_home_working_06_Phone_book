import user_interface
import input_interpreter as inputs
import logger

def add():
    print("Add ")
    name = inputs.name()
    phone = inputs.phone()
    comment = inputs.comment()
    logger.log(name, phone, comment)

def view():
    logger.view("all") # Закладка для поиска по контактам


def save():
    with open('phone_book.csv', 'r') as file:
        phone_book = file.read()
    format = input("Введите имя файла: ")
    with open(format, 'w') as new_file:
        new_file.write(phone_book)
        print("Данные сохранены в файл.")



    print("Save ")

def imp():
    print("Import ")

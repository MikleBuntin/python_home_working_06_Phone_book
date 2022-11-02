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


def save(): # Доступные форматы: .txt, .csv, .html
    new_file_name = input("Введите имя файла: ")
    new_file_name = new_file_name.split('.')
    if new_file_name[1] == "txt":
        logger.save_to_txt(new_file_name[0])
    elif new_file_name[1] == "csv":
        logger.save_to_csv(new_file_name[0])
    elif new_file_name[1] == "html":
        logger.save_to_html(new_file_name[0])





    print("Save ")

def imp():
    print("Import ")

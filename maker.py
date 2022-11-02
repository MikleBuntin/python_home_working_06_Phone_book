import user_interface
import input_interpreter as inputs
import logger
import saver
import file_importer as f_imp

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
        saver.save_to_txt(new_file_name[0])
    elif new_file_name[1] == "csv":
        saver.save_to_csv(new_file_name[0])
    elif new_file_name[1] == "html":
        saver.save_to_html(new_file_name[0])
    else:
        print("Формат не поддерживается. ")
def imp():
    file_name = input("Введите имя файла: ")
    file_name = file_name.split('.')
    if file_name[1] == "txt":
        f_imp.imp_txt(file_name[0])
    elif file_name[1] == "csv":
        f_imp.imp_csv(file_name[0])
    elif file_name[1] == "html":
        f_imp.imp_html(file_name[0])
    else:
        print("Формат не поддерживается. ")

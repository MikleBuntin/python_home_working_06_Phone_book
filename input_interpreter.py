
def name():
    name = input("Введите имя: ")
    return name

def phone():
    while not phone.isdigit():
        phone = input("Введите телефон: ")
    return phone

def comment():
    comment = input("Комментарий: ")
    return comment

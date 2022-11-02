
def name():
    name = input("Введите имя: ")
    return name

def phone():
    phone = "a"
    while not phone.isdigit():
        phone = input("Введите телефон: ")
        if not phone.isdigit():
            print("Используйте только цифры")
    return phone

def comment():
    comment = input("Комментарий: ")
    return comment

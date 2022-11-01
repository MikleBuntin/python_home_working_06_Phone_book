import maker as make

def command(comm):
    if comm == "add":
        make.add()
    elif comm == "view":
        make.view()
    elif comm == "save":
        make.save()
    elif comm == "import":
        make.imp()
    else:
        print("!!! Неизвестная команда. !!!")


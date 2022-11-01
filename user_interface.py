
def ask_command(): # выдать список команд, запросить команду, преобразовать к нужному виду и отдать.
    print("Доступные команды:", "View - просмотр книги", "Import - импорт книги из файла", "Add - добавление записи", "Save - сохранить книгу в файл", "Q - Выход" sep='\n')
    in_command = str(input("Введите команду: "))
    # print("in_command.lower(): ", in_command.lower())
    return in_command.lower()

def view(command):
    print("command: ", command)
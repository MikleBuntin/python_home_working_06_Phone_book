import logger

def imp_txt(f_name):
    with open(f_name + ".txt", 'r') as file:
        for line in file:
            if len(line) > 3:
                line = line.replace("Name: ", "")
                line = line.replace(", phone: ", ";")
                line = line.replace(" - ", ";")
                line = line.replace("\n", "")
                line = line.split(';')
                logger.log(line[0], line[1], line[2])
                print("array: ", line)

        # phone_book = file.read()
        # print("book: ", phone_book)
        # for line in file:
        #     # array = list(line.split(';'))
        #     # name =
        #     print(line.rindex('name: '))
        #     print(line.index(' phone: '))



    # with open(f_name + ".txt", 'w') as new_file:
    #     new_file.write(phone_book)
    #     print("Данные сохранены в файл {}.txt.".format(f_name))


def log(name, phone, comment):
    with open('phone_book.csv', 'a') as file:
        file.write("{};{};{}\n".format(name, phone, comment))

    print("Абонент {} с номером {} ({}) добавлен".format(name, phone, comment))



# def save_to_csv(f_name):
#     with open('phone_book.csv', 'r') as file:
#         phone_book = file.read()
#     with open(f_name + ".csv", 'w') as new_file:
#         new_file.write(phone_book)
#         print("Данные сохранены в файл {}.csv.".format(f_name))
#
# def save_to_html(f_name):
#     with open('phone_book.csv', 'r') as file:
#         style = 'style="font-size:30px;"'
#         phone_book = '<html>\n  <head></head>\n  <body>\n'
#         for line in file:
#             line = line.split(';')
#             phone_book += '    <p {}>Name: {}, phone: {} ({}) </p>\n' .format(style, line[0], line[1], line[2])
#         phone_book += '  </body>\n</html>'
#
#     with open(f_name + ".html", 'w') as new_file:
#         new_file.write(phone_book)
#         print("Данные сохранены в файл {}.html.".format(f_name))

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


def imp_csv(f_name):
    with open(f_name + ".csv", 'r') as file:
        for line in file:
            if len(line) > 3:
                line = line.split(';')
                logger.log(line[0], line[1], line[2])


def imp_html(f_name):
    with open(f_name + ".html", 'r') as file:
        for line in file:
            line = line.replace("<html>\n  <head></head>\n  <body>\n", "")
            line = line.replace('style="font-size:30px;', '')
            line = line.replace("    <p {}>Name: ", "")
            line = line.replace(", phone: ", ";")
            line = line.replace(" (", ";")
            line = line.replace(") </p>\n", "")
            line = line.replace("< / body >\n < / html >", "")
            line = line.split(';')
            if len(line) >= 3:
                logger.log(line[0], line[1], line[2])


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

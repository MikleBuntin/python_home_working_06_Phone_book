def save_to_txt(f_name):
    with open('phone_book.csv', 'r') as file:
        phone_book = ''
        for line in file:
            if len(line) > 3:
                line = line.split(';')
                phone_book += 'Name: {}, phone: {} - {}' .format(line[0], line[1], line[2])


    with open(f_name + ".txt", 'w') as new_file:
        new_file.write(phone_book)
        print("Данные сохранены в файл {}.txt.".format(f_name))



def save_to_csv(f_name):
    with open('phone_book.csv', 'r') as file:
        phone_book = file.read()
    with open(f_name + ".csv", 'w') as new_file:
        new_file.write(phone_book)
        print("Данные сохранены в файл {}.csv.".format(f_name))

def save_to_html(f_name):
    with open('phone_book.csv', 'r') as file:
        style = 'style="font-size:30px;"'
        phone_book = '<html>\n  <head></head>\n  <body>\n'
        for line in file:
            if len(line) > 3:
                line = line.split(';')
                phone_book += '    <p {}>Name: {}, phone: {} ({}) </p>\n' .format(style, line[0], line[1], line[2])
        phone_book += '  </body>\n</html>'

    with open(f_name + ".html", 'w') as new_file:
        new_file.write(phone_book)
        print("Данные сохранены в файл {}.html.".format(f_name))

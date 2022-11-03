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
            if line.rfind('Name') > 0:
                name = line[line.find('Name: ') + 6: line.find('phone') - 2]
                line = line[line.find('phone'):]
                phone = line[line.find('phone: ') + 7: line.find('(')]
                line = line[line.find('('):]
                comment = line[line.find('(') + 1: line.find(')')]
                logger.log(name, phone, comment)

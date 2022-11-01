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
    # user_interface.view()
    print("View ")

def save():
    print("Save ")

def imp():
    print("Import ")


class InvalidIntException(Exception):
    def __init__(self, arg):
        super().__init__('not integer : {}'.format(arg))

def convert_to_integer(text):
    if text.isdigit():
        return int(text)
    else:
        raise InvalidIntException(text)

if __name__ == '__main__':
    try:
        print("input number :")
        text = input()
        number = convert_to_integer(text)
    except InvalidIntException as err:
        print("exception occurred ({})".format(err))
    else:
        print("convert into integer : {}({}".format(number, type(number)))

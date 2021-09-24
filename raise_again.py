
def some_function():
    print("input number 1-10: ")
    num = int(input())
    if num < 1 or num > 10:
        raise Exception("invalid number: {}".format(num))
    else:
        print("input number is {}.".format(num))

def some_function_caller():
    try:
        some_function()
    except Exception as err:
        print("1) exception occurred. {}".format(err))
        raise

try:
    some_function_caller()
except Exception as err:
    print("2) exception occurred. {}".format(err))
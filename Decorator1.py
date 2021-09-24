
class MyDecorator:
    def __init__(self, f):
        print("initializing MyDecorator...")
        self.func = f

    def __call__(self, *args, **kwargs):
        print("Begin : {}".format(self.func.__name__))

        self.func()

        print("End : {}".format(self.func.__name__))


def print_hello():
    print("Hello")

print_hello = MyDecorator(print_hello)

print_hello()
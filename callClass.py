
class Callable:
    def __call__(self, *args, **kwargs):
        print("I am called")

obj = Callable()
obj()
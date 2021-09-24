
class A:
    def __init__(self):
        print("A.__init__()")
        self.message = "Hello"

class B(A):
    def __init__(self):
        A.__init__(self)
        print("B.__init__()")


obj = B()
print(obj.message)

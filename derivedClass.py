
class Base:
    def base_method(self):
        print("base_mothod")

class Derived(Base):
    pass


base = Base()
base.base_method()
derived = Derived()
derived.base_method()

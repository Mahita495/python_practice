class Base:
    def __init__(self):
        self.a="Welcome"
        self.__c ="Hello"

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private members of base class")
        print(self.__c)

obj = Base()
print(obj.a)
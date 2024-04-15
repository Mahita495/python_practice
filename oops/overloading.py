class car:
    def maruti(self):
        print("maruti car with type alto")
class swift(car):
    def __init__(self,type):
        self.type=type
    def maruti(self):
        print("maruti car of type swift")

c=car()
s=swift(car)
c.maruti()
s.maruti()

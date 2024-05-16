class Bird:
    def intro(self):
        print("Birds")
    
    def flight(self):
        print("Some birds can fly but some can't")

class sparrow(Bird):
    def flight(self):
        print("Sparrow can fly")

class ostrich(Bird):
    def flight(self):
        print("Ostrich can't fly")

bird = Bird()
s=sparrow()
o=ostrich()
s.flight()
bird.flight()
o.flight()

s.intro()

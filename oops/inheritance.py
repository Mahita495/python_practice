class parent:
    def __init__(self,parentname):
        self.parentname=parentname
    def attribute(self):
        print("I'm a parent with name "+self.parentname)
class child(parent):
    def __init__(self,childname,parentname):
        self.childname=childname

        parent.__init__(self,parentname)

    def printname(self):
        print("Father name: " + self.parentname)
        print("Son's name: "+ self.childname)

s1=child('abc','dfg')
print(s1.parentname)
s1.printname()

    
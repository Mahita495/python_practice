class Student:
    def __init__(self,name,rollno,marks1,marks2) -> None:
        self.name=name
        self.rollno=rollno
        self.marks1=marks1
        self.marks2=marks2
        
    def accept(self, name, rollno, marks1,marks2):
        obj= Student(name,rollno, marks1,marks2 )
        ls.append(obj)
    
    def search(self, rno):
        for i in range(len(ls)):
            if ls[i].rollno == rno:
                return i

    def display(self,obj):
        print("Name : ", obj.name)
        print("RollNo : ", obj.rollno)
        print("Marks1 : ", obj.marks1)
        print("Marks2 : ", obj.marks2)
        print("\n")

    def delete(self, rno):
        i=self.search(rno)
        del ls[i]

    def update(self,rn,new_rn):
        i=self.search(rn)
        ls[i].rollno=new_rn

ls=[]
obj = Student(" ",0,0,0)

print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")

obj.accept("A", 1, 100, 100)
obj.accept("B", 2, 90, 90)
obj.accept("C", 3, 80, 80)
 
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    obj.display(ls[i])
 
# elif(ch == 3):
print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])
 
# elif(ch == 4):
obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
    obj.display(ls[i])
 
# elif(ch == 5):
obj.update(3, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
    obj.display(ls[i])
 
# else:
print("Thank You !")
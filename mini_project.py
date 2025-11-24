class Persen:
    def __init__(self,name,age,roll_num):
        self.name = name
        self.age = age
        self.roll_num = roll_num
        print("Persen consturction called: ")
    def details(self):
        print(f"MY name is {self.name} and MY age is {self.age} and MY roll_num is {self.roll_num}")
class Student(Persen):
    def __init__(self,name,age,roll_num):
        super().__init__(name,age,roll_num)
        print("Student consturction called: ")
class Teacher(Persen):
    def __init__(self,name,age,roll_num):
        super().__init__(name,age,roll_num)
        print("Teacher consturction called: ")
class Staff(Persen):
    def __init__(self,name,age,roll_num):
        super().__init__(name,age,roll_num)
        print("Staff consturction called: ")
p1 = Persen("afzal",21,409)
S1 = Student("abc",2,9)
T1 = Teacher("ab",1,4)   
S2 = Staff("al",21,49)
print(p1.__dict__)
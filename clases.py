class Person:
    def __init__(self,name,language):
        self.name=name
        self.language=language
        print("init Person")
    def talk(self):
        print(f"Hi I am {self.name} and I'm learning {self.language}")

class Student(Person):
    def __init__(self,name,language):
        self.name=name
        self.language=language
        print("init Student")
    def talk(self):
        print(f"I'm {self.name} and I'm a student")
        

#p1 = Person("Mai","Spanish")
#p1.talk()

s1 = Student("Amy","none")
s1.talk()




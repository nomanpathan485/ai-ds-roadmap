class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"my name is {self.name}, and i am {self.age} years old.")

#objects

s1 = student("Noman", 20)
s2 = student("xyz",32)
s1.introduce()
s2.introduce()    
        
# Definition of Class
# 
# 
# studentName # Camel Case
# StudentName # Pascal Case

class Human:
    def __init__(self):
        print("Parent is called!")

class Student(Human):  

    name : str = ""
    age : str = ""
    address : str = ""

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        super().__init__()

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address : {self.address}"


obj_or_instance = Student("Sagar sedai", 20, "Singapore") 

print(obj_or_instance)

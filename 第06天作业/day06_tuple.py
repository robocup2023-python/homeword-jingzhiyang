class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def __str__(self):
        return f"{self.name} is {self.age} years old and is {self.gender}"


class Student(Person):
    def __init__(self, name, age, gender, college, clazz):
        super().__init__(name,age,gender)
        self.college = college
        self.clazz = clazz
        
    def __str__(self):
        return f"{self.name} is {self.age} years old {self.gender} student of {self.college} {self.clazz} class"
    
print(Person("Danny",19,"male"))
print(Student("Mary",18,"female","xjtu","computer science"))

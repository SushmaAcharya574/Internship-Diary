class Person:
    def __init__(self, name):
        self.name = name
        print("Person Constructor Called")

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)   # Constructor chaining
        self.roll = roll
        self.marks = 0
        print("Student Constructor Called")

    # Method chaining methods
    def set_marks(self, marks):
        self.marks = marks
        return self   # enables chaining

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}")
        return self   # enables chaining

    def grade(self):
        if self.marks >= 90:
            print("Grade: A")
        elif self.marks >= 75:
            print("Grade: B")
        else:
            print("Grade: C")
        return self   # enables chaining


# Driver Code
s = Student("Sushma", 101)

# Method chaining in action
s.set_marks(85).display().grade()

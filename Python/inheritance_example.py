# Base Class
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")


# -------------------------------
# 1. Single Inheritance
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def show_student(self):
        print(f"Roll No: {self.roll}")


# -------------------------------
# 2. Multilevel Inheritance
class GraduateStudent(Student):
    def __init__(self, name, roll, degree):
        super().__init__(name, roll)
        self.degree = degree

    def show_degree(self):
        print(f"Degree: {self.degree}")


# -------------------------------
# 3. Hierarchical Inheritance
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show_teacher(self):
        print(f"Subject: {self.subject}")


# -------------------------------
# 4. Multiple Inheritance
class Sports:
    def __init__(self, sport):
        self.sport = sport

    def show_sport(self):
        print(f"Sport: {self.sport}")


class Result(Student, Sports):   # Multiple Inheritance
    def __init__(self, name, roll, marks, sport):
        Student.__init__(self, name, roll)
        Sports.__init__(self, sport)
        self.marks = marks

    def show_result(self):
        print(f"Marks: {self.marks}")


# -------------------------------
# 5. Hybrid Inheritance
class SchoolMember(Result, Teacher):  # Hybrid (multiple + hierarchical)
    def __init__(self, name, roll, marks, sport, subject):
        Result.__init__(self, name, roll, marks, sport)
        Teacher.__init__(self, name, subject)

    def display_all(self):
        self.show_name()
        self.show_student()
        self.show_result()
        self.show_sport()
        self.show_teacher()


# -------------------------------
# Driver Code

print("\n--- Single Inheritance ---")
s = Student("Sushma", 101)
s.show_name()
s.show_student()

print("\n--- Multilevel Inheritance ---")
g = GraduateStudent("Anu", 102, "B.Tech")
g.show_name()
g.show_student()
g.show_degree()

print("\n--- Hierarchical Inheritance ---")
t = Teacher("Ravi", "Math")
t.show_name()
t.show_teacher()

print("\n--- Multiple Inheritance ---")
r = Result("Priya", 103, 88, "Cricket")
r.show_name()
r.show_student()
r.show_result()
r.show_sport()

print("\n--- Hybrid Inheritance ---")
sm = SchoolMember("Kiran", 104, 92, "Football", "Science")
sm.display_all()

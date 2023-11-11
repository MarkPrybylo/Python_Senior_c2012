# class Human():
#     def __init__(self, name):
#         self.name = name
#     type = "human"
#
#
# class Student(Human):
#     age = 15
#     university = "IT Step"
#
#
# class Worker(Human):
#     age = 30
#     place = "EA"
#
#
# andriy = Student(name="Andriy")
# mykola = Worker(name="Mykola")
# print(f"Student: {andriy.name}, type: {andriy.type}, age: {andriy.age}, learns in {andriy.university}.")
# print(f"Worker: {mykola.name}, type: {mykola.type}, age: {mykola.age}, works in {mykola.place}.")
# class University:
#     name = "ITSTEP"
#
#
# class Group(University):
#     def __init__(self, groupname):
#         self.groupname = groupname
#
#
# class Teacher(University):
#     def __init__(self, name, age, subject):
#         self.name = name
#         self.age = age
#         self.subject = subject
#     def getInfo(self):
#         print(f"Teacher: {self.name}, age: {self.age}, teaching {self.subject}")
#     def changeSubject(self):
#         newsubject = input("Select new subject: ")
#         self.subject = newsubject
#
#
# class Student(Group):
#     def __init__(self, name, age, groupname, grades):
#         self.name = name
#         self.age = age
#         self.groupname = groupname
#         self.grades = grades
#     def getInfo(self):
#         print(f"Student: {self.name}, age: {self.age}, in group: {self.groupname}, grades: {self.grades}")
#     def changeGroup(self):
#         newgroupname = input("Select new group: ")
#         self.groupname = newgroupname
#
#
# class Subject(Teacher, Student):
#     students_learning = 0
#     teachers_teaching = 0
#
#
# c2012 = Group("c2012")
# stepan = Student("Stepan", 15, "c2012", [1, 12, 9])
# danylo = Teacher("Danylo", 25, "Unity")
#
# u_input = ""
# while u_input != "stop":
#     u_input = input("Choose action:\n   getteacher - get teacher's info\n   getstudent - get student's info\n"
#                     "   teachersubject - change teacher's subject\n   studentgroup - change student's group\nYour action: ")
#     if u_input == "getteacher":
#         danylo.getInfo()
#     elif u_input == "teachersubject":
#         danylo.changeSubject()
#     elif u_input == "getstudent":
#         stepan.getInfo()
#     elif u_input == "studentgroup":
#         stepan.changeGroup()
#     else:
#         print("Unknown command")

class Student():
    def __init__(self, age):
        self.age = age


class Grades(Student):
    def __init__(self, grades, password):
        self.grades = grades
        self.__password = password
    def getpassword(self):
        secretcode = input("Input secret code to see password: ")
        if secretcode == "a23":
            print(self._Grades__password)
        else:
            print(len(self._Grades__password) * "*")
    def getgrades(self):
        u_password = input("Input password to see grades: ")
        if u_password == self._Grades__password:
            print(self.grades)
        else:
            print("Wrong password")


a = Student(12)
b = Grades([1, 12, 3, 9], "bober228")
action = input("Your action: ")
if action == "getage":
    print(a.age)
if action == "getpassword":
    b.getpassword()
if action == "getgrades":
    b.getgrades()
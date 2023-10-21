# a = int(input("Input num: "))
# b = 0
# i = 0
# while b <= 100:
#     print(b)
#     b += a
#     i += 1
# print(f"I added {a} {i} times")
# class Student:
#     def __init__(self, name, age=12):
#         self.name = name
#         self.age = age
#         print(f"Name: {self.name}, age: {self.age}")
#
# zlata = Student(name="Zlata", age=13)
# marko = Student(name="Marko")
# class Animal:
#     def __init__(self, type, weight):
#         self.type = type
#         self.weight = weight
#     def call(self):
#         print(f"Type: {self.type}, weight: {self.weight} kg")
# dog = Animal(type="dog", weight=50)
# dog.call()
#
# cat = Animal(type="cat", weight=25)
# cat.call()
#
# parrot = Animal("parrot", 10)
# parrot.call()
#
# capybara = Animal(type="capybara", weight=40)
# capybara.call()
made_movies = 0
class Movie:
    def __init__(self, name, views, length, madein):
        global made_movies
        made_movies += 1
        self.name = name
        self.views = views
        self.length = length
        self.producer_country = madein
        print(
            f"New movie! Name: {self.name}, views: {self.views}, length: {self.length} hours, made in {self.producer_country}")

breaking_bad = Movie("Breaking Bad", 0, 2.5, "USA")
squid_game = Movie("Squid Game", 0, 3, "South Korea")
print(f"Made movies in total: {made_movies}")
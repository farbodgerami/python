from secrets import choice

class Student:
    educational_platform= 'udemy'
    def __init__(self,name,age=34):
        self.name=name
        self.age=age

    def greet(self):
        greetings=['a {}','b {}','c {}']

        greeting=choice(greetings)
        return greeting.format(self.name)

# helper class:
# def classcreate(studentnames):
#     # returns a list of student names
#     return [Student(name) for name in studentnames]
names=['james','lars','luis']
classinstances=[Student(name) for name in names]

# for student in classcreate(names):
for student in classinstances:
    print(student.greet())
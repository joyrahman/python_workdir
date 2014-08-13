class student:
    age = 0
    sex = "M"
    def __init__(self,age=20):
        self.age = age
    def area(self):
        return self.age*self.age



'''
main class
'''

joy = student(23)

print joy.age
print student.age
print joy.sex
print student.area(joy)

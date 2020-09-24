# Inheritance (Kalıtım): Miras alma

class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print('Person Created')

    def whoAmI(self):
        print('I am a person')

class Student(Person):      # Person'ın sahip olduğu tüm özelliklere sahip
    pass

class Student2(Person):
    def __init__(self, fname, lname, number):
        self.studentNumber = number
        Person.__init__(self, fname,lname)
        print('Student Created')

    # override_temel sınıftaki metodu ezer
    def whoAmI(self):
        print('I am a student')

    def sayHello(self):
        print('Hello I am a student')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        # super().__init__(fname, lname)  #self yazmaya gerek yok
        self.branch = branch
        print('Teacher Created')

    def whoAmI(self):
        print(f'I am a {self.branch} teacher')


p1 = Person('Onur', 'Karagüler')
print('**************')
s1 = Student('İlkay', 'Karagüler')
print('**************')
s2 = Student2('Umut', 'Karagüler', 1256)
print('**************')
t1 = Teacher('Defne', 'Karagüler', 'Math')
print('**************')
print(p1.fname + ' ' + p1.lname)
print(s1.fname + ' ' + s1.lname)
print(s2.fname + ' ' + s2.lname + ' ' + str(s2.studentNumber))

p1.whoAmI()
s1.whoAmI()
s2.whoAmI()
s2.sayHello()
t1.whoAmI()

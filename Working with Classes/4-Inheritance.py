# inheritance allows us to inherit attributes and methods from a parent class
# we can create subclasses and get all functionality of the parent class
# we can overwrite or add completely new functionality without affecting the parent class
# we want to create developers and managers. Both of them are going to have names, email addresses and a salary
# Employee class already has them. instead of copying all this into subclasses,
# we can reuse that code by inheriting from employee

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):       # attributes of the class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@hotmail.com'

    def fullname(self):     # this is a method
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)        # self.raise_amount is global variable

# inherit from the Employee class. even without any code in the Developer class,
# it will have all of the attributes and methods of the Employee class
class Developer(Employee):
    pass

dev_1 = Employee('Onur', 'Karaguler', 50000)       # instance
dev_2 = Employee('Ilkay', 'Karaguler', 40000)

print(dev_1.email)
print(dev_2.email)

print('=====')
# the two developers were created successfully
# we can access the attributes that were actually set in our parent employee class
dev_1 = Developer('Onur', 'Karaguler', 50000)       # instance
dev_2 = Developer('Ilkay', 'Karaguler', 40000)

print(dev_1.email)
print(dev_2.email)

# print(help(Developer))
# the instances first look at Develop class for the init method. when it does not find there,
# then they look at the Employee class and find it there
'''
 |  Method resolution order: 
 |      Developer
 |      Employee
 |      builtins.object
'''

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print('=====')
# when we want to customize the subclass
# when we want the developers to have a raise amount of 10%
class Developer(Employee):
    raise_amt = 1.10

dev_1 = Developer('Onur', 'Karaguler', 50000)       # instance
dev_2 = Developer('Ilkay', 'Karaguler', 40000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print('=====')
# to initiate a subclasses with more information than the parent class
# the Employee class only accepts firstname, lastname and pay.
# we also want to pass in a programming language there
# we are going to have to give the developer class its own init method

class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):    # add in an argument 'prog_lang'
        """
        self.first = first
        self.last = last
        self.pay = pay
        instead of copying all of them from the Employee class and pasting into the Developer class,
        we want to let the Employee class's init method handle them.
        """
        super().__init__(first, last, pay)
        # it is going to pass the arguments to the Employee's init method,
        # and let that class handle those arguments
        # Employee.__init__(self, first, last, pay) will also work
        self.prog_lang = prog_lang

dev_1 = Developer('Onur', 'Karaguler', 50000, 'Python')
dev_2 = Developer('Ilkay', 'Karaguler', 40000, 'Java')

print(dev_1.email)
print(dev_2.prog_lang)

print('=====')
# give an option of passing in a list of employees that this manager supervises

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
print(mgr_1.print_emp())
mgr_1.add_emp(dev_2)
mgr_1.rem_emp(dev_1)
print(mgr_1.print_emp())

print('=====')
print(isinstance(mgr_1, Manager))       # True
print(isinstance(mgr_1, Employee))      # True
print(isinstance(mgr_1, Developer))     # False

print('=====')
print(issubclass(Manager, Employee))       # True
print(issubclass(Manager, Developer))      # False
print(issubclass(Developer, Employee))     # True

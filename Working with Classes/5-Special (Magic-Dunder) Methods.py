# these special methods allow us to emulate some built_in behavior with in Python
# it is also how we implement operator overloading

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
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):     # should be used for debugging and logging
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"
        # print out 'Employee('Onur', 'Karaguler', '50000')'

    def __str__(self):      # more readable for an end user
        return f"{self.fullname()} - {self.email}"
        # this will print out 'Onur Karaguler - Onur.Karaguler@hotmail.com'
        # instead of __repr__

    def __add__(self, other):       # self is the left side , other is the right side of the addition
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Onur', 'Karaguler', 50000)
emp_2 = Employee('Ilkay', 'Karaguler', 40000)

print(emp_1)
# it prints out <__main__.Employee object at 0x7f8ad81444f0>
# we can change this behavior to print out something a little more user-friendly
# that is what the special methods are going to allow us to do
# these special methods are always surrounded by double underscores (dunder) (__init__)
# two more common special methods (__repr__ and __str__)

print(repr(emp_1))
print(str(emp_1))
print(emp_1.__repr__())
print(emp_1.__str__())

print('=====')
# there are also a lot of special methods for arithmetic
print(1 + 3)    # Actually it is using a special method in the background called __add__
print(int.__add__(1, 3))
print(str.__add__('a', 'b'))

print('=====')
# if we want to be able to calculate total salaries just by adding employees together
print(emp_1 + emp_2)        # we added two employee objects together
# without __add__ method, it will give us an error
# https://docs.python.org/3/reference/datamodel.html

print('=====')
print(len('test'))
print('test'.__len__())

print(len(emp_1))










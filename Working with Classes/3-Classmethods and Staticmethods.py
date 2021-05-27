# regular methods in a class automatically take the instance as the first argument
# by convention we are calling this 'self'. How can we change this?
# automatically takes the class as the first argument
# to turn a regular method into a class method, adding a decorator to the top '@classmethod'

class Employee:

    num_of_emp = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):       # attributes of the class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@hotmail.com'

        Employee.num_of_emp += 1

    def fullname(self):     # this is a method
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)        # self.raise_amount is global variable

    @classmethod        # we receive the class as the first argument instead of the instance
    def set_raise_amt(cls, amount):     # we are working the class instead of the instance
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)       # cls and Employee are basically same things, create an object

    @staticmethod
    def is_workday(day):
        if (day.weekday() == 5) or (day.weekday() == 6):      # saturday and sunday
            return False
        return True


emp_1 = Employee('Onur', 'Karaguler', 50000)       # instance
emp_2 = Employee('Ilkay', 'Karaguler', 40000)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print('=====')
# if we want to change 'raise_amount' to 1.05
Employee.set_raise_amt(1.05)        # it is the same thing 'Employee.raise_amt = 1.05'
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print('=====')
# this is a common use for how someone is using the class.
# we have a three strings that are employees separated by hyphens
emp_str_1 = 'Onur-Karaguler-70000'
emp_str_2 = 'Ilkay-Karaguler-50000'
emp_str_3 = 'Umut-Karaguler-30000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)

# we do not have to parse these strings every time
# create a new classmethod 'from_string'. use this method as an alternative constructor
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

print('=====')
# STATIC CLASS
# they do not pass an instance or class automatically
# they behave just like regular functions except we include them in our classes
# because they have some logical connection with the class

# if we want a simple function that will take in date and
# return whether or not that was a work day
# that has a logical connection to the employee class
# but it does not depend on any specific instance or class variable
# we are going to make a static method '@staticmethod'

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))     # returns True

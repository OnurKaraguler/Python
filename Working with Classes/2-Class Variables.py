class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):       # attributes of the class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@hotmail.com'

        Employee.num_of_emp += 1

    def fullname(self):     # this is a method
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)        # self.raise_amount is global variable


emp_1 = Employee('Onur', 'Karaguler', 50000)       # instance
emp_2 = Employee('Ilkay', 'Karaguler', 40000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# the class variable can be accessed from both the class itself and instances
# when we try to access an attribute on an instance, it will first check if the instance contains that attribute.
# if it does, then it will see if the class or any class that it inherits from contains that attribute.

print(emp_1.__dict__)
# {'first': 'Onur', 'last': 'Karaguler', 'pay': 52000, 'email': 'Onur.Karaguler@hotmail.com'}
# there is no raise_amount in this list

print(Employee.__dict__)
# {'__module__': '__main__', 'raise_amount': 1.04, ..... }
# the class contains raise_amount attribute. That is the value the instances see

print('=====')
Employee.raise_amount = 1.05        # it changes the raise_amount for the class and all of the instances

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print('=====')
# what if I was to set the raise_amount using an instance
emp_1.raise_amount = 1.06        # it changes the raise_amount for the emp_1
print(emp_1.__dict__)
# the emp_1 has raise_amount  within its name space equal to 1.06
# it finds this within its own name space and returns that value before going and searching the class

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print('=====')
# if I create a class variable 'num_of_emp', each time we create an employee,
# I am going to increment that by one.

print(Employee.num_of_emp)      # because we created 2 employees








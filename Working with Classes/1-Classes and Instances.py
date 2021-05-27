class Employee:
    def __init__(self, first, last, pay):       # attributes of the class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@hotmail.com'

    def fullname(self):     # this is a method
        return f"{self.first} {self.last}"



em_1 = Employee('Onur', 'Karaguler', 50000)       # instance
em_2 = Employee('Ilkay', 'Karaguler', 40000)

print((em_1.email))
print((em_2.email))

print(em_1.fullname())










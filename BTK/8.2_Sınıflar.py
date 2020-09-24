# class Person:
#     #class attributes
#     address = 'no information'
#
#     #constructor (yapıcı metod)- oluşturulan herbir obje için çalıştırılır
#     def __init__(self, name, year):     #self: class'tan üretilen objeleri teslim eder
#
#         # object attributes
#         self.name = name
#         self.year = year
#         print('init metodu çalıştı')
#
#     #instance methods
#     def intro(self):
#         print('Hello there. I am ' + self.name)
#
#     def calculateAge(self):
#         return 2019 - self.year
#
# #object(instance)
# p1 = Person(name='ali', year=1990)
# p2 = Person(name='yağmur', year=1995)
#
# #updating
# p1.name = 'ahmet'
# p1.address = 'kocaeli'
#
# #accessing object attributes
# print(f'name: {p1.name} year: {p1.year} address: {p1.address}')
# print(f'name: {p2.name} year: {p2.year} address: {p2.address}')
#
# p1.intro()
# p2.intro()
#
# print(f'yaşım: {p1.calculateAge()}')
# print(f'yaşım: {p2.calculateAge()}')
#
# #==================================

class Circle:
    # class object attributes
    pi = 3.14

    def __init__(self, yaricap=1):      # Eğer belirtilmediyse yarıçap Oyun_1 olarak kabul edilsin
        self.yaricap = yaricap

    # Methods
    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap

    def alanHesapla(self):
        return self.pi * self.yaricap**2

c1 = Circle()   # yarıçap = Oyun_1
c2 = Circle(5)

print(f'c1: alan = {c1.alanHesapla()} çevre = {c1.cevreHesapla()}')
print(f'c2: alan = {c2.alanHesapla()} çevre = {c2.cevreHesapla()}')

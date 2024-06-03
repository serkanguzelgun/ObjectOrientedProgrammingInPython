'''
#class
class Person:

    # class attributes
    address = 'no information'
    #constructor(yapıcı metod)
    def __init__(self,name,year):
        # object attributes
        self.name=name
        self.year=year
        print('init metodu çalıştı')
    #methods
    def intro(self):
        print('Hello There. I am ' + self.name)

    def calculateAge(self):
        return 2019 - self.year
#object(instance)
p1 = Person('Ali',1990)
p1.intro()

print(f'yaşım: {p1.calculateAge()} , adım: {p1.name}')

#updating
p1.name = 'Ahmet'
p1.address = 'Kocaeli'

#accessing object attributes
print(f'name: {p1.name} , year: {p1.year} , address:{p1.address}')
print(p1)
print(type(p1))

 '''

class Circle:
    #Class object attribute
    pi = 3.14

    def __init__(self,yaricap=1):
        self.yaricap = yaricap

    # Methods
    def cevre_hesapla(self):
        return 2 * self.pi + self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle() #yaricap=1
c2 = Circle(5)

print(f'c1 : alan = {c1.alan_hesapla()} , çevre = {c1.cevre_hesapla()}')
print(f'c2 : alan = {c2.alan_hesapla()} , çevre = {c2.cevre_hesapla()}')
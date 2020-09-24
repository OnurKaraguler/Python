def add(*params):
    print(params[0])
    print(params[2])
    return sum((params))

print(add(10,20,30,40,50,60))

def add2(*params):
    sum = 0
    for n in params:
        sum += n
    return sum

print(add2(10,20,30,40,50,60))

def displayUser(**params):   #**args da olur
    for key, value in params.items():
        print(f'{key} is {value}')


displayUser(name = 'Onur', age = 43, city = 'İstanbul')
displayUser(name = 'İlkay', age = 43, city = 'İstanbul', phone = '05558468265')
displayUser(name = 'Umut', age = 12, city = 'İstanbul', phone = '---', email = 'i.karaguler@hotmail.com')
displayUser(name = 'Defne', age = 12, city = 'İstanbul')


def myFunc(a,b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, key1 = 'value Oyun_1', key2 = 'value 2')
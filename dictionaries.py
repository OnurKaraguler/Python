students = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(students)

# get a value of one key
print(students['name'])
print(students.get('name'))
print(students.get('phone'))  # if it does not exist, get method returns none instead of an error.
print(students.get('phone', 'Not Found'))  # we can also specify a default value for keys that do not exist

# add a key and value
students['phone'] = '555-5555'

# update a value
students['name'] = 'Jane'   # the value for name was updated
print(students)

# update with one statement
students.update({'name': 'John', 'age': 26, 'phone': '666-6666'})
print(students)

# delete a specific key and value
del students['phone']
print(students)

students.pop('age')
print(students)

# how many keys are there?
print(len(students))
print(students.keys())  # see the key names
print(students.values())  # see the values
print(students.items())  # see the keys and  values

# loop
for key in students:    # it just looped through and printed out all of the keys
    print(key)
for key, value in students.items(): # print out keys and values
    print(key, value)








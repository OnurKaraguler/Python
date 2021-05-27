# the function returning a list
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


my_num = square_numbers([1, 2, 3, 4, 5])
print(my_num)


# how can we convert this to be a generator
def square_numbers(nums):
    for i in nums:
        yield (i * i)  # yield keyword makes it a generator


my_num = square_numbers([1, 2, 3, 4, 5])
print(my_num)  # <generator object square_numbers at 0x7f86d0042190>
# generators do not hold the entire result in memory.
# it yields one result at a time
print(next(my_num))  # prints out '1'
print(next(my_num))  # prints out '4'. each time that we run next it gets the next value that's yielded

print('=====')
for num in my_num:
    print(num)

print('=====')
# list comprehension generator
my_num = (x * x for x in [1, 2, 3, 4, 5])
print(my_num)

# convert the generator to a list
print(list(my_num))  # but we loose the advantages that we gain in terms of performance

# a generator is better with performance, because it does not hold all values in memory
# if it is a small list like this, generator is not a big deal
# if we have tens of thousands or even millions of items to loop through,
# having that many items in memory will definitely be noticeable

# EXAMPLE
import resource
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print(f'Memory (Before): {round(memory_usage * 9.537 * 10 ** -7, 2)}Mb')


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


t1 = time.time()
people = people_generator(1000000)
t2 = time.time()

memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print(f'Memory (Generator): {round(memory_usage * 9.537 * 10 ** -7, 2)}Mb')
print(f'Took {round(t2 - t1, 2)} Seconds')

t1 = time.time()
people = people_list(1000000)
t2 = time.time()

memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print(f'Memory (List): {round(memory_usage * 9.537 * 10 ** -7, 2)}Mb')
print(f'Took {round(t2 - t1, 2)} Seconds')


# FIBONACCI NUMBERS
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for f in fib():
    if f > 50:
        break
    print(f)

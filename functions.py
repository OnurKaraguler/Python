def hello_func():
    print('Hello Function!')

hello_func()  # run function

print('=====')
def hello_func():
    return 'Hello Function!'

print(hello_func().upper())

print('=====')
# pass argument to the function, we need to create some parameters within the parentheses
def hello_func(greeting):
    return f'{greeting} Function!'

print(hello_func('Hi'))     # greeding variable equals to the string 'Hi'

print('=====')
# default value
def hello_func(greeting, name='You'):
    return f'{greeting} {name}!'

print(hello_func('Hi'))     # without a value for name argument
print(hello_func('Hi', name='Onur'))

print('=====')
# allowing us to accept an arbitrary number of positional or keyword arguments
# we do not know how many of these positional and keyword arguments there will be
# that's why *args, **kwargs are used
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info(*courses, **info)      # add * in front of courses and ** in front of info

# EXAMPLE

# Number of days per month. First value placeholder for indexing purposes.
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month-1]

print(days_in_month(2000, 2))













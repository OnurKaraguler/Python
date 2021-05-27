# CLOSURES

def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)

    return inner_func()

outer_func()

print('=====')
# now let's do something different
def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)

    return inner_func   # let's just return the function without executing it

outer_func()    # it does not look like anything happened
my_funk = outer_func()      # assign this to a variable. The variable is actually a function.
print(my_funk.__name__)      # It is equal to the inner_func

my_funk()       # It can be executed. It prints out the message of hi. So that is closure
# a closure is an inner function that remembers and has access to variables in the local scope

print('=====')
# let's add some parameters
def outer_func(msg):
    message = msg
    def inner_func():
        print(message)

    return inner_func   # let's just return the function without executing it

hi_funk = outer_func('Hi')
hello_funk = outer_func('Hello')

hi_funk()
hello_funk()

print('=====')
# DECORATORS

def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function()
    return wrapper_function

def display():
    print('display function run')

decorator_display = decorator_function(display)
decorator_display()

print('=====')
def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function()
    return wrapper_function

@ decorator_function        # this is equal to display = decorator_function(display)
def display():
    print('display function run')

display()


print('=====')
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function

@ decorator_function
def display1():
    print('display function run')

@ decorator_function
def display_info(name, age):
    print(f'display info run with arguments ({name}, {age})')

display_info('Onur', 44)
# display()

print('=====')
# class decorator

class DecoratorClass(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)

@ DecoratorClass
def display1():
    print('display function run')

@ DecoratorClass
def display_info(name, age):
    print(f'display info run with arguments ({name}, {age})')

display_info('Onur', 44)
# display()












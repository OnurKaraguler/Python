'''
LEGB (
Local (variables defined within a function),
Enclosing (variables in the local scope of enclosing functions),
Global (the top level of a module),
Built-ins (names that are preassigned in Python)

Python first check Local, then Enclosing, Global, lastly Built-ins
'''

x = 'global x'      # it is a global variable, because it is in the main of the file
def test():
    y = 'local y'   # it is a local variable
    print(y)
    print(x)        # it can be printed out because it is global

test()

# print(y)      # we will get an error
print(x)        # it will work

print('=====')
def test2():
    x = 'local x'   # global x variable will not be overwritten,
    # print(y)      # this just creates a local X variable only with in the function
    print(x)

test2()
print(x)

print('=====')
# if we want to set a new value for that global X variable from within the test2 function
# just add 'global x1' at the top of the test2 function
x1 = 'global x'
def test2():
    global x1        # if x1 global variable doe not exist, this set it within the test function
    x1 = 'local x'   # global x variable will be overwritten,
    # print(y)      # this just creates a local X variable only with in the function
    print(x1)

test2()
print(x1)

print('=====')
def test3(z):           # z is a local variable
    x = 'local x'
    print(z)

test3('local z')

# ---> BUILT-INS
print('=====')
# min is a built-ins function
m = min([5, 1, 4, 2, 3])
print(m)

# ---> ENCLOSING
def outer():
    x = 'outer x'
    def inner():
        # x = 'inner x'
        print(x)        # first checks x variable in the inner function.
    inner()             # if there is not, it checks in the enclosing functions
    print(x)

outer()

print('=====')
def outer2():
    x = 'outer x'
    def inner():
        nonlocal x      # change the x = 'outer x' variable
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer2()
print(x)        # global variable














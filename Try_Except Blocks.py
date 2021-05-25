try:
    f = open('File Objects - Reading and Writing to Files/text_file.txt')
except Exception:
    print('Sorry. This file does not exist')

print('=====')
try:
    f = open('File Objects - Reading and Writing to Files/text.txt')    # run successfully
    var = bad_var       # this is what through the exception
except Exception:       # Exception is general
    print('Sorry. This file does not exist')

print('=====')
try:
    f = open('File Objects - Reading and Writing to Files/text.txt')    # run successfully
    # var = bad_var       # we will get an error
except FileNotFoundError:
    print('Sorry. This file does not exist')       # It will not execute code

print('=====')
try:
    f = open('File Objects - Reading and Writing to Files/text.txt')    # run successfully
    var = bad_var       # we will get an error
except FileNotFoundError:
    print('Sorry. This file does not exist')
except Exception:
    print('Sorry. Something went wrong')

print('=====')
try:
    f = open('File Objects - Reading and Writing to Files/text.txt')    # run successfully
    var = bad_var       # we will get an error
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

print('=====')
try:
    f = open('File Objects - Reading and Writing to Files/text.txt')    # run successfully
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:       # if we do not throw an exception
    print(f.read())
    f.close()

print('=====')
try:
    f = open('File Objects - Reading and Writing to Files/text_file.txt')    # run successfully
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
finally:       # it runs no matter what happens, for example, close down a database
    print('Executing Finally...')

print('=====')
try:
    f = open('File Objects - Reading and Writing to Files/text.txt')    # run successfully
    if f.name == 'File Objects - Reading and Writing to Files/text.txt':
        raise Exception     # manually raise Exceptions
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:       # it runs no matter what happens, for example, close down a database
    print('Executing Finally...')




"""
Comparisions:
Equal               ==
Not Equal           !=
Greater or Equal    >=
Less or Equal       <=
Object Identity     is
"""

# language = 'Python'
language = 'Java'
if language == 'Python':    # == we are testing for equality. this will evaluate True or False
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('no match')

# boolean operations (and, or, not)
user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:       # both of those evaluated to True, 'or' only one needed to be true
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:       # 'not' switches true to false
    print('Please log in')
else:
    print('Welcome')

"""
False Values:
    False
    None
    Zero
    Any empty sequence. For example, '', (), []
    Any empty mappint. For example, {}
"""
condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')




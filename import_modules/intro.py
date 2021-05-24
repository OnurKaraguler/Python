import sys

# import a module (alternative_1)
# sys.path.append('/Users/onurkaraguler/Desktop/git_repos/Python/for_beginners/import_modules/myModule')
# from my_module import find_index, test

# import a module (alternative_2)
from myModule.my_module import find_index, test
import random, math, datetime, calendar, os

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

print(sys.path)  # list of directories Python looks for modules when we run import

# ---> Standard Libraries
# random module
courses = ['History', 'Math', 'Physics', 'CompSci']
random_course = random.choice(courses)
print(random_course)

# math module
rads = math.radians(90)
print(rads)
print(math.sin(rads))

# datetime/calendar module
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

# os module
print(os.getcwd())
print(os.__file__)

import antigravity



import os

'''
file names were:
    Automate Parsing and Renaming of Multiple Files.py
    Jupiter - Our Solar System - #6.txt
    Earth - Our Solar System - #4.txt
     Mercury - Our Solar System - #2.txt
     Mars - Our Solar System - #5.txt
'''

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    if f_ext != '.py':
        f_title, f_course, f_num = f_name.split('-')
        f_title = f_title.strip()
        f_course = f_course.strip()
        f_num = f_num.strip()[1:].zfill(2)    # [1:] do not get the first character, zfill(2) add 0 to the beginning

        new_name = f'{f_num}-{f_title}{f_ext}'
        print(new_name)

        os.rename(f, new_name)      # it replaced the old file names with the new ones

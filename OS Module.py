import os
from datetime import datetime

# print(dir(os))  # all attributes and methods

print(os.getcwd())  # get current working directory

os.chdir('/Users/onurkaraguler/Desktop/git_repos/Python/')  # change directory
print(os.getcwd())  # cwd is Python folder
print(os.listdir())  # files and folders

try:
    # create a folder
    os.mkdir('OS-Demo')  # create only one folder
    os.mkdir('OS-Demo/Sub-Dir')  # create the folder, if OS-Demo exists
    # os.makedirs('OS-Demo/Sub-Dir')  # create the both OS-Demo and Sub-Dir folders (if OS-Demo does not exist)
except:
    pass

# remove a folder
# os.rmdir('OS-Demo/Sub-Dir')
# os.rmdir('OS-Demo')
# os.removedirs('OS-Demo/Sub-Dir')

try:
    # rename a folder
    os.rename('OS-Demo/Sub-Dir', 'OS-Demo/Sub-Dir_renamed')
except:
    pass

# the size of a folder
print(os.stat('OS-Demo/Sub-Dir_renamed').st_size)
# modification time
mod_time = os.stat('OS-Demo/Sub-Dir_renamed').st_mtime  # returns a timestamp
print(mod_time)
print(datetime.fromtimestamp(mod_time))     # print out a human readable form

# to see the entire directory tree
for dirpath, dirnames, filenames in os.walk('/Users/onurkaraguler/Desktop/git_repos/Python/for_beginners'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)

print('=====')
# access environment variables
print(os.environ.get('HOME'))

# create a file within the home directory
file_path = os.path.join(os.environ.get('HOME'), 'sil.txt')
print(file_path)
# with open (file_path, 'w') as f:
#     f.write()

print('=====')
# get the basename of an entire path
print(os.path.basename('/tmp/test.txt'))
# get the directory of an entire path
print(os.path.dirname('/tmp/test.txt'))
# get the both
print(os.path.split('/tmp/test.txt'))
# check if the path exists
print(os.path.exists('/tmp/test.txt'))
# check if it is a directory or file
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
# split the file root and extension
print(os.path.splitext('/tmp/test.txt'))
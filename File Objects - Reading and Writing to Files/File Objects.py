# open the file for reading

# it will automatically close the file
with open('File Objects - Reading and Writing to Files/text.txt', 'r') as f:
    f_content = f.read()
    print(f_content)

print('=====')
# what if we have an extremely large file that we want to read
# but we do not want to load all of the contents of that file into memory
# we get a list of all of the lines in the file
with open('File Objects - Reading and Writing to Files/text.txt', 'r') as f:
    f_content = f.readlines()
    print(f_content)

print('=====')
# instead of readlines, we can do readline. readline grapped the first line of the file
# everytime that we run readline, it gets the next line in our file
with open('File Objects - Reading and Writing to Files/text.txt', 'r') as f:
    f_content = f.readline()
    print(f_content, end='')

    f_content = f.readline()
    print(f_content, end='')

print('=====')
# this is efficient because it is not reading in all of the contents from the file all at once
# so it is not a memory issue that we have to worry about that
with open('File Objects - Reading and Writing to Files/text.txt', 'r') as f:
    for line in f:
        print(line, end='')

print('=====')
# it printed out the first 100 characters of the file instead of printing the whole thing
with open('File Objects - Reading and Writing to Files/text.txt', 'r') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_content, end='')
        f_contents = f.read(size_to_read)

# writing the file (create a new file or write on it)
with open('File Objects - Reading and Writing to Files/text2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)   # overwrite the T
    f.write('R')

# copy a file
with open('File Objects - Reading and Writing to Files/text.txt', 'r') as rf:
    with open('File Objects - Reading and Writing to Files/text_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# # copy a picture
# with open('File Objects - Reading and Writing to Files/bronx.jpg', 'rb') as rf:
#     with open('File Objects - Reading and Writing to Files/bronx_copy.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)







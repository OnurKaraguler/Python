# -----> LISTS
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

# How many values in our list
print(len(courses))

# We can access each of these values
print(courses[0])  # first item
print(courses[-1])  # last item
print(courses[:2])  # a range of values (first index is inclusive but last index is not)
print(courses[2:])

# to add an item
courses.append('Art')  # to the end of the list
print(courses)
courses.insert(0, 'Art')  # to a specific location in the list, first argument is location
print(courses)

# to add multiple values
courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)  # add the entire list oc courses_2, not individual value (list in a list)
print(courses)
courses.extend(courses_2)  # extend courses with courses_2
print(courses)

# remove some values
courses.remove('Math')  # 'Math' is removed from the courses
print(courses)
courses.pop()  # remove the last value
print(courses)

# count a specific item in the list
print(courses.count('Art'))

# reverse the list
courses.reverse()
print(courses)

# sort the list
courses.pop()
courses.sort()  # strings are sorted alphabetically
print(courses)
courses.sort(reverse=True)  # strings are sorted in reverse order
print(courses)

nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)  # numbers are sorted in ascending order
nums.sort(reverse=True)
print(nums)  # numbers are sorted in descending order

# There is also a way that we can get a sorted version of our list without altering the original list
courses = ['History', 'Math', 'Physics', 'CompSci']
sorted(courses)  # the list is not sorted
print(courses)

sorted_courses = sorted(courses)  # to get the sorted list we have to make a new variable
print(sorted_courses)

# min, max and sum
print(min(nums))
print(max(nums))
print(sum(nums))

# index of a certain value
print(courses.index('CompSci'))  # we get 3
print('Art' in courses)  # we get False

# access the index and the value
for index, course in enumerate(courses, start=1):
    print(index, course)
# turn the list into strings
course_str = ' - '.join(courses)
print(course_str)

# turn the string back into a list
new_list = course_str.split(' - ')
print(new_list)

# Mutable
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = courses
courses[0] = 'Art'  # change courses' first value
print(courses)
print(courses_2)  # change courses_2's first value as well

# -----> TUPLES
# Tuples are very similar to lists but with one major difference. We can not modify tuples.
# Immutable
courses = ('History', 'Math', 'Physics', 'CompSci')
courses_2 = courses
# courses[0] = 'Art'      # get an error. it is immutable. we cannot append, remove.
print(courses)
print(courses_2)  # change courses_2's first value as well

# -----> SETS
# set values that are unordered and have no duplicates
courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(courses)  # it prints out of values. These are not in the order like in the list.
# This order can change with each execution. Sets throw away duplicates
print('Math' in courses)  # We could do that with lists and tuples also. But sets are optimized for this.

# intersection, difference, union
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# Empty List
empty_list = []  # empty_list = list()

# Empty Tuple
empty_tuple = ()  # empty_tuple = tuple()

# Empty Sets
empty_set = set()  # empty_set = {} is not right. It is a dict.

#-----ragne
# A = list(range(0,20,3))
# print(A)

#-----enumerate ----> index numarasına göre listeleme
# greeting = 'Hello'
#
# for index, item in enumerate(greeting):
#     print(f'index: {index} letter: {item}')

#-----zip (index numarasına göre)
list1 = [1,2,3,4,5]
liste2 = ['a', 'b', 'c', 'd', 'e']
print(list(zip(list1,liste2)))

for a,b in zip(list1,liste2):
    print(a)
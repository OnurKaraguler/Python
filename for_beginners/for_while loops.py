# ---> FOR LOOP
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

print('======')
# break statement
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

print('======')
# continue statement
for num in nums:
    if num == 3:
        print('Found!')
        continue            # skip to the next iteration
    print(num)

print('======')
# loop with in loop
for num in nums:
    for letter in 'ab':
        print(num, letter)

print('======')
# range
for i in range(3):      # range(1:5) start at 1 and goes up to 4
    print(i)

print('======')
# ---> WHILE LOOP
x = 0
while x < 5:
    print(x)
    x += 1

print('======')
x = 0
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1
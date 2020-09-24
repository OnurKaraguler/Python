userA = ["Sadık", 36]
userB = ["Çınar",2]

users = [userA, userB]

print(users[0])
print(users[1])
print(users[0][0])


numbers = [1,10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val1 = min(numbers)
val2 = max(numbers)
val3 = min(letters)     # Alfabetik sıraya göre belirler
val4 = max(letters)
val5 = numbers[3:6]

numbers[4] = 40         # Listede 4 -> 40 olur
numbers.append(49)      # Listenin sonuna 49 eklenir
numbers.insert(3, 78)   # index numarasına göre 78 sayısı eklenir
numbers.insert(-1, 52)   # sondaki sayıyı sağa kaydırır ve 52 sayısı eklenir

numbers.pop()           # son eleman silinir
numbers.pop(0)          # ilk eleman silinir
numbers.remove(10)      # listeyi arar ilk 10 sayıyı siler

numbers.sort()          # listeyi sıralar
letters.sort()
numbers.reverse()       # listeyi ters sıralar
letters.reverse()


print(val1, val2)
print(val3, val4)
print(val5)
print(numbers)
print(letters)
print(len(numbers))     # listedeki unsur adedi
print(len(letters))
print(numbers.count(10))    # listede kaç adet 10 var
print(letters.count("a"))    # listede kaç adet a var
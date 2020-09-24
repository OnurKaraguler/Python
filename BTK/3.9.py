website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberleriniz (40 saat) "

# kaç karakter var
result1 = len(course)

# www karakterlerini al
result2 = website[7:10]

# com karakterlerini al
length = len(website)
result3 = website[length-3:length]

# ilk ve son 15  karakterlerini al
result4 = course [:15]
result5 = course [-15:]

# tersten yazdırma
result6 = course [::-1]

# Değişkenler ile ekrana yazdırma
name, surname, age, job = "Onur", "Karagüler", 42, "mühendis"
result7 = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}"

# "Hello world" dekli w->W ile değiştir
s = "Hello world"
result8 = s[0:6] + "W" + s[-4:]

# abc ifadesini 3 defa yan yana yaz
result9 = "abc" * 3



print(result1)
print(result2)
print(result3)
print(result4, result5)
print(result6)
print(result7)
print(result8)
print(result9)

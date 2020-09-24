# with open("newfile.txt", "r+", encoding='utf-8') as file:
#     file.write("finding_word")                                    # 0. konumdan itibaren finding_word yazar

# with open("newfile.txt", "r+", encoding='utf-8') as file:
#     file.seek(20)
#     file.write("finding_word")                                    # 20. konumdan itibaren finding_word yazar

# with open("newfile.txt", "r+", encoding='utf-8') as file:       # r+ okuma ve yazma
#     print(file.read())

# with open("newfile.txt", "a", encoding='utf-8') as file:       # sona ekler
#     file.write("\nYeter Karagüler")

# with open("newfile.txt", "r+", encoding='utf-8') as file:       # başa ekler
#     content = file.read()                             # içeriği ekleyelim
#     content = "Hüseyin Karagüler\n" + content
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt", "r+", encoding='utf-8') as file:
#     list = file.readlines()                             # içeriği ekleyelim
#     list.insert(Oyun_1, "Yadigar Karagüler\n")
#     file.seek(0)
#     for i in list:
#         file.write(i)
#     print(list)

with open("newfile.txt", "r+", encoding='utf-8') as file:
    list = file.readlines()                             # içeriği ekleyelim
    list.insert(1, "Yadigar Karagüler\n")
    file.seek(0)
    file.writelines(list)
    print(list)

# with open("newfile.txt", "r", encoding='utf-8') as file:       # daha sonra okumak için
#     print(file.read())
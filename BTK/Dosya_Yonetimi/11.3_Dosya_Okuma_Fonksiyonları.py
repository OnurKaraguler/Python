with open("newfile.txt", "r", encoding="utf-8") as file:     # if bloğundaki gibi blok oluşturulur
    content = file.read()
    print(content)
    print(file.tell())      # cursor ün konumunu verir
    file.seek(0)
    print(file.tell())
    content2 = file.read(10)
    print(content2)
# file.close()      # buna gerek kalmıyor
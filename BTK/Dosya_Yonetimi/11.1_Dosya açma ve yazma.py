# Dosya açmak ve oluşturmak için open() fonksiyonu oluşturulur.
# Kullanımı: open(dosya_adi, dosya_erisme_modu)
# dosya_erisme_modu => dosyayı hangi amaçla açtığınızı belirtir.

# 'w': (Write) yazma modu. Dosyayı konumunda oluşturur. Önceki veri silinir ve yeniden eklenir.

# file = open("newfile.txt", "w")
# file.close()        # Dosya kapatılmalı

# file = open("C:/Python_Examples/BTK/BTK_QT/Dosya_Yonetimi/newfile.txt", "w")    # Belirli bir konuma
# print(file)

# file = open("newfile.txt", "w", encoding='utf-8')
# file.write('Onur Karagüler')
# file.close()

# 'a': (Append) ekleme. Dosyayı konumunda yok ise oluşturur.

# file = open("newfile.txt", "a", encoding='utf-8')
# # file.write('\nOnur Karagüler')
# file.write('Onur Karagüler\n')
# file.close()

# 'x': (Creat) oluşturma. Dosya konumunda zaten var ise hata verir.

# file = open("newfile2.txt", "x", encoding='utf-8')

# 'r': (Read) okuma. Varsayılan dosya konumunda yok ise hata verir.
# try:
#     file = open("newfile.txt", "r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı")
#     file.close()

file = open("newfile.txt", "r", encoding='utf-8')

# for döngüsü
# for i in file:
#     print(i, end="")        # boş satır ekleme

# content1 = file.read()
#
# print("içerik Oyun_1")
# print(content1)             # dosya açık olduğundan kursor sonda
#
# content2 = file.read()
#
# print("içerik 2")
# print(content2)         # kursor sonda olduğundan içerik boş geldi

# content = file.read(5)
# content2 = file.read(3)
# print(content, content2)

# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")     # her seferinde Oyun_1 satır okunur

liste = file.readlines()
print(liste)
print(liste[0])
print(liste[1])
file.close()

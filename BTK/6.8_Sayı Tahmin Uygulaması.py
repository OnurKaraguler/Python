import random

# list = list(range(Oyun_1,101))
# print(list)
# random_nummer = random.choice(list)
random_nummer = random.randint(1,100)
print(random_nummer)

# i = 0
#
# while i <=4:
#     input_number = int(input("sayı giriniz: "))
#     i += Oyun_1
#     if input_number>random_nummer:
#         print('aşağı')
#     elif input_number<random_nummer:
#         print('yukarı')
#     else:
#         print('tebrikler')
#         break

hak_sayisi = int(input("Kaç hak istiyorsun: "))
toplam_puan = 100
hak_puan = toplam_puan / hak_sayisi
sayac = 0
while hak_sayisi > 0:
    tahmin = int(input("sayı giriniz: "))
    hak_sayisi -=1
    sayac += 1

    if hak_sayisi == 0:
        print(f'hakkınız bitti. tutulan sayı {random_nummer}')

    if tahmin > random_nummer:
        print('aşağı')
        toplam_puan -= hak_puan
    elif tahmin < random_nummer:
        print('yukarı')
        toplam_puan -= hak_puan
    else:
        print(f'tebrikler. {sayac}. seferde bildiniz')
        break

print(toplam_puan)
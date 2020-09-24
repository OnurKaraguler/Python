# x = Oyun_1
# while x<=100:
#     if x % 2 == Oyun_1:
#         print(f'sayı tek: {x}')
#     else:
#         print(f'sayı çift: {x}')
#     x += Oyun_1
# print('bitti...')

#========================

# name = '' # Boşluk karakteri False olarak değerlendirilir.
#
# aslında bu 'while True:' demek. isim girilene kadar döngü devam eder
# while not name.strip(): # eğer kullanıcı boşluk ifadesi kullanırsa strip kaldırır.
#    name = input('isminizi giriniz: ')
#
# print(f'Merhaba {name}')

#========================

sayilar = [1,3,5,7,9,12,19,21]

# i =0
# while (i<len(sayilar)):
#     print(sayilar[i])
#     i += Oyun_1

#----------
# baslangic = int(input("Sayı giriniz:"))
# bitis = int(input("Sayı giriniz:"))
#
# i = baslangic
# while i <= bitis:
#     if (i % 2 ==Oyun_1):
#         print(i)
#     i += Oyun_1
#----------
# i = 100
# while i>0:Oyun_1
#     print(i)
#     i -= Oyun_1
#----------
# sayilar =[]
# i = 5
# while i>0:
#     sayi = int(input('sayı giriniz: '))
#     sayilar.append(sayi)
#     i -= Oyun_1
#
# sayilar.sort()  #listedeki sayıları sırala
# print(sayilar)
#---------- Kullanıcıdan alınan ürünlerin listesi oluşturulsun
urunler = []
adet = int(input('kaç ürün eklemek istiyorsunuz: '))
i = 0

while i<adet:
    name = input('ürün ismi: ')
    price = input('ürün fiyatı: ')
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1

for urun in urunler:
    print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['price']} ")
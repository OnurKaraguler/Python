# def yazdir(kelime, adet):
#     print(kelime * adet)
#
# yazdir('Merhaba\n',3)
# # yazdir( input('kelime giriniz:'+'\n'), int(input('kaç kez tekrarlasın: ')))
#
# def listeyeCevir(*params):
#     liste = []
#
#     for param in params:
#         liste.append(param)
#
#     return liste
#
# result = listeyeCevir(10,20,30,'Merhaba')
# print(result)

#-----asal sayı bul
# def asalSayilariBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+Oyun_1):
#         if sayi > Oyun_1:    #asal işlemine tabi olacak
#             for i in range(2,sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)
#
# sayi1 = int(input('sayı Oyun_1: '))
# sayi2 = int(input('sayı 2: '))
#
# asalSayilariBul(sayi1,sayi2)

#-----tam bölenleri bulma

def tamBolenleriBul(sayi):
    tamBolenler = []
    for i in range(2,sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler

print(tamBolenleriBul(int(input('sayı Oyun_1: '))))
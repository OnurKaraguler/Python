sayi = int(input('sayi: '))

if sayi == 1:
    print(('Oyun_1 sayisi asal değildir'))
asalmi = True #varsayalım girilen sayi asal

for i in range(2,sayi):
    if (sayi % i == 0):
        asalmi = False
        break

if asalmi:
    print('sayı asaldır.')
else:
    print('sayı asal değildir')

#------sadece tek sayıların toplamı
x = 0
toplam = 0
while x<=100:
    x += 1
    if (x % 2 == 0):
        continue
    toplam += x

print(toplam)
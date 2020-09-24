sayilar = [1,3,5,7,9,12,19,21]

#for i in sayilar:
#    if i%3 == 0:
#        print(i)

toplam = 0
#for i in sayilar:
#    toplam +=i
#print(toplam)

A =[]
for i in sayilar:
    if i%2 == 1:
        #print(i**2)
        A.append(i**2)
print(A)

sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

B =[]
for j in sehirler:
    if (len(j)<=5):
        B.append(j)
        #print(j)
print(B)

urunler = [
    {'name':'samsung S6', 'price':'3000'},
    {'name': 'samsung S7', 'price': '4000'},
    {'name': 'samsung S8', 'price': '5000'},
    {'name': 'samsung S9', 'price': '6000'},
    {'name': 'samsung S10', 'price': '7000'}
]

toplam_fiyat=0
for m in urunler:
    toplam_fiyat += int(m['price'])
print('toplam ürün fiyat:',toplam_fiyat)

C=[]
for n in urunler:
    if (int(n['price']) <= 5000):
        #print(n['name'])
        C.append(n['name'])
print(C)
from datetime import datetime
from datetime import timedelta      # ileri tarihi hesaplamak için
# from datetime import date
# from datetime import time
# import datetime       # tüm modülleri import ediyor
print('===================BTK====================')
# simdi = datetime.now()      # datetime.now()=datetime.today()
# print(simdi.year)
# print(simdi.month)
# print(simdi.day)
# print(simdi.hour)
# print(simdi.minute)
# print(simdi.second)

# result = datetime.ctime(simdi)
# result = datetime.strftime(simdi,'%Y')         # String olarak veriyor
# result = datetime.strftime(simdi,'%X')
# result = datetime.strftime(simdi,'%d')
# result = datetime.strftime(simdi,'%A')
# result = datetime.strftime(simdi,'%B')
# result = datetime.strftime(simdi,'%Y %B %A')    # https://www.w3schools.com/python/python_datetime.asp
# print(result)

# t = '21 Nisan 2019'         # elimizde bir obje var diyelim
# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)

# veya

# t = '15 April 2019 hour 10:12:30'           # ingilizce olacak
# dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
# print(dt)
# print(dt.year)

# birthday = datetime(1977,10,20,12,30,00)     # kendimiz de tarih oluşturabiliriz
# print(birthday)
# result = datetime.timestamp(birthday)   # tarihi saniye cinsinden verir
# result = datetime.fromtimestamp(result)     # saniye yi tarih cinsine geri çevirir
# result = datetime.fromtimestamp(0)          # saniye 1970 ten itibaren hesaplanır.
simdi = datetime.now()

# result = simdi - birthday       # timedelta dan gelen bilgi
# # result1 = result.days
# result1 = result.seconds
# print(result, result1)

# result = simdi + timedelta(days=10)         # ileri tarih hesaplaması için timedelta yı import etmen gerekli
# result = simdi + timedelta(days=750)
result = simdi - timedelta(days=10)
print(result)
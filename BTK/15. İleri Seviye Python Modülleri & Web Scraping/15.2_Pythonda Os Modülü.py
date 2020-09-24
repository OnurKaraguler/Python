import os       # işletim sistemi ile ilgili bilgi sunar.
import datetime

# result = dir(os)
# result = os.name        # İşletim sistemini söyler
# result = os.getcwd()    # şu an çalışılan dosya ile ilgili bilgi verir
# os.mkdir('new_directory')       # aynı dizin içerisinde klasör oluşturuldu

# os.chdir('C:\\')        # C dizinine yönlendirirsek
# os.mkdir('new_directory')       # C dizini içerisinde klasör oluşturuldu

# os.chdir('..')      # bir üst dizine geçer
# os.chdir('..')      # bir sonraki üst dizine geçer
# os.chdir('../..')      # bu da aynı görevi yerine getirir
# result = os.getcwd()
# print(result)

# os.makedirs('new_directory/new')        # iç içe klasörler oluşturur('C:\\' dizin yazarak da oluşturulur)

# result = os.listdir()       # çalışılan klasördeki içeriği listeler
# result = os.listdir('C:\\')     # dizini listeler
# print(result)

# for dosya in os.listdir():
#     if dosya.endswith('.py'):       # sadece py uzantılı dosyaları gösterir
#         print(dosya)

# result = os.stat('15.1_Pythonda Datatime Modülü.py')        # st_size=boyut(byte), st_atime=son erişilme, st_mtime=oluşturulma
# # result = result.st_size/1024        # Kb cinsinden dosya boyutu
# # result = datetime.datetime.fromtimestamp(result.st_ctime)   # dosyanın oluşturulma tarihi
# # result = datetime.datetime.fromtimestamp(result.st_atime)   # dosyanın son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)   # dosyanın değiştirilme tarihi
# print(result)

# os.system('notepad.exe')        # istenilen sistem program açılır
# os.system('calc.exe')

# os.rename('newdirectory','newDirectory')
# os.rmdir('newDirectory/new')        # dizin boş olması gerekli
# os.removedirs('newDirectory/new2')         # alt klasörü siler

# result = os.path.abspath('15.1_Pythonda Datatime Modülü.py')        # dosyanın tam yolunu verir
# result = os.path.dirname('C:/Python_Examples/BTK/Genel/15. İleri Seviye Python Modülleri & Web Scraping/15.1_Pythonda Datatime Modülü.py')
# dosyanın dizin ismini verir
# result = os.path.dirname(os.path.abspath('15.1_Pythonda Datatime Modülü.py'))   # doğru kullanımı
# result = os.path.exists('15.1_Pythonda Datatime Modülü.py')     # var mı yok mu
# result = os.path.isdir('C:/Python_Examples/BTK/Genel/15. İleri Seviye Python Modülleri & Web Scraping/')
# dizin midir?
# result = os.path.isfile('C:/Python_Examples/BTK/Genel/15. İleri Seviye Python Modülleri & Web Scraping/15.1_Pythonda Datatime Modülü.py')
# dosya mıdır?

# result = os.path.join('C:\\','1','2')       # Dizin yolu oluşturulur.
# result = os.path.split('C:\\deneme')        # yolu böler
result = os.path.splitext('15.1_Pythonda Datatime Modülü.py')   # uzantısını böler
print(result[0], result[1])

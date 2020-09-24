anamessage = "Hello There. My name is Sadık Turan"

message1 = anamessage.upper()          # Büyük harfe çevirir
message2 = anamessage.lower()          # Küçük harfe çevirir
message3 = anamessage.title()          # İlk harfleri büyük
message4 = anamessage.capitalize()     # Sadece ilk harf büyük
message6 = anamessage.split()          # Boşluklardan parçalara ayırma
message7 = anamessage.split(".")       # "." lardan parçalara ayırma
message8 = " ".join(message6)          # Parçalara boşluk ekleyerek birleştirme
infound = anamessage.startswith("H")   # Mesaj H ile başlıyor ise TRUE
infound2 = anamessage.endswith("n")    # Mesaj n ile bitiyor ise TRUE


# yanlışlıkla boşluk karakteri girildiğinde
anamessage2 = " Hello There. My name is Sadık Turan"
message5 = anamessage2.strip()

index = anamessage.find("Sadık")    # İlk harfin index numarasını verir.
print(index)                        # Listede yok ise -Oyun_1 numarası görülür

# Cümle içerisinde değişiklik
anamessage3 = anamessage.replace("Sadık","Çınar")
print(anamessage3)

# 50 karakterlik alana mesajı ortalar
anamessage4 = anamessage.center(50)
anamessage5 = anamessage.center(50,"*")     # sağa ve sola * koyar
print(anamessage4)
print(anamessage5)

print(message2)
print(message3)
print(message4)
print(message5)
print(message6)
print(message7)
print(message8)
print(infound, infound2)
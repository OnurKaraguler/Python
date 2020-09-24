import random

result = random.random()    # 0.0 - Oyun_1.0 arasında
result = random.random() * 100
result = random.uniform(10,100)         # 10 ile 100 arası ondalıklı sayılar
result = int(random.uniform(10,100))    # 10 ile 100 arasında tam sayılar
result = random.randint(1,100)          # Oyun_1 ile 100 arasında tam sayılar

print(result)

greeting = 'hello there'
names = ['ali', 'ahmet', 'hasan', 'ayşe']
result = names[random.randint(0,len(names))]

result = random.choice(names)
result2 = random.choice(greeting)

print(result,result2)

liste = list(range(10))
random.shuffle(liste)       # listeyi karıştırır
print(liste)

liste = range(100)
result = random.sample(liste, 3)        # rastgele 3 tane sayı getirir
result2 = random.sample(names,2)
print(result, result2)
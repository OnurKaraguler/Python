def tambolenbulma(number):
    tam_bolenler = []

    for i in range(2, number):
        if number % i == 0:
            tam_bolenler.append(i)
    return tam_bolenler


while True:
    sayi = input("Sayı:")

    if sayi == "q":
        break
    else:
        sayi = int(sayi)
        print(tambolenbulma(sayi))

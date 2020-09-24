def yasHesapla(dogumYili):
    return 2020 -dogumYili

ageOnur = yasHesapla(1977)
print(ageOnur)

def EmekliligeKacYilkaldi(dogumYili, isim):
    '''
    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı
    INPUT: Doğum yılı
    OUTPUT: Hesaplanan yıl bilgisi
    '''

    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
         print(f'{isim} Bey emekliliğinize {emeklilik} yıl kaldı')
    else:
        print(f'{isim} Bey zaten emeklisiniz')

Onur_emeklilik = EmekliligeKacYilkaldi(1977, 'Onur')
print(Onur_emeklilik)

print(help(EmekliligeKacYilkaldi))
##Function 
#definiton
def ortalamaHesapla():
    final =80
    vize=59
    ortalama = (vize*0.4) + (final*0.6)
    print(ortalama)

ortalamaHesapla()

def ortalamaHesapla2() -> float:
    final =80
    vize=59
    ortalama = (vize*0.4) + (final*0.6)
    return ortalama #geriye dönecek değer

print(ortalamaHesapla2())

def ortalamaHesaplaVeDondur(vize: float, final:float) -> float:
    return (vize*0.4) + (final*0.6)

print(ortalamaHesaplaVeDondur(85,45)) 
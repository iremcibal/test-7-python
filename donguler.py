#For

#0'dan başlatalım 10'dan küçük olana kadar döngü çalışsın 
for i in range(0,10):
    print(i)


#sayilar arasındaki en büyüğünü bulalım 
""" biggestValue = 0
for i in range(10):
    sayi = int(input(f"{i+1}. sayiyi griniz: "))
    if sayi > biggestValue:
        biggestValue = sayi


print(f"Girdiğiniz sayilar arasından en büyük olanı: {biggestValue}") """


""" sayilar = []
for i in range(3):
    sayilar.append(int(input(f"{i+1}. sayiyi griniz: ")))


sayilar.sort(reverse=True)
enBuyuk = int(input("Sayılar arasından en büyük kaçıncı elemanı istiyorsun?"))
print(sayilar[enBuyuk-1]) """

#[180,250,270]

#start,stop,step => range fonknun parametreleri
""" forRangeMin = int(input("Döngünün alt limitini belirleyiniz"))
forRangeMax = int(input("Döngünün üst limitini belirleyiniz"))

for i in range(forRangeMin,forRangeMax+1):
    if i % 2 == 0 :
        print(i) """


ogrenciler = ["ibrahim","simge","bilge","nursena"]
#0 1 2 3 
#4
print(len(ogrenciler))

for i in range(len(ogrenciler)):
    print(f"{i+1}. öğrenci {ogrenciler[i]}")

for ogrenci in ogrenciler:
    print(f"öğrenci: {ogrenci}")

#break => ilgili döngünün o anda bitirilmesini,kırılmasını sağlar
for i in range(len(ogrenciler)):
    if i>2:
        break
    print(f"{i+1}. öğrenci: {ogrenciler[i]}")

#continue => iterasyondaki o anki değeri atla bir sonraki değere geç
for i in ogrenciler:
    if i == "ibrahim":
        continue
    print(f"ögrenci: {i}")



#while
i=0
while i<10:
    print("Merhaba")
    i=i+1 #i++


#while True:
#    print("merhaba")



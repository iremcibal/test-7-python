print("Merhaba Etiyalilar") 
#yorum satiri 
print("Hoşgeldiniz")

#degiskenler 
print("Hoşgeldiniz UserName")
#string - metinsel değer
text = "Merhaba,Hoşgeldiniz"
print(text)
print(text)
print(text)
print(text)
print(text)

studentCount = "45"
print(studentCount + "5")

#int,integer => numerik - tam sayı ifade eder
studentCount = 45 
print(studentCount + 5)

#double,float,decimal => ondalıklı sayılar
averagePoint = 25.5
print(averagePoint + 5)

#Boolean,bool => True-False => 1,0
isVerified = True
print(isVerified)

print(type(text))
print(type(studentCount))
print(type(averagePoint))
print(type(isVerified))

#Matematiksel Operatörler
# + - * / %

number= 10
print(number + number)
print(10+ 10)
print(number + 10)

print(number -2)

print(number * 2)

print(number / 2)

#mod operatörü 
print(number % 4)

print(number + ((10-number) * (5/10))) 

#Mantıksal Operatörler - KArşılaştırma operatörler

print(10 == 10) #True
print(11 == 10) #False

print(10 != 10) #false
print(11 != 10) #true

print(number>10) #false
print(number>=10) #true

print(number< 10) #false
print(number<= 10) #true


#string interpolation => metin birleştirme

hello = "Merhaba"
userName = "irem"

totalText = hello + " " +userName
print(totalText)


totalText = "{message} Sayın {name}".format(message=hello,name=userName)
print(totalText)

#f-string
totalText = f"Hoşgeldiniz {userName}"
print(totalText)



print("----------------------------------------")
#Dizi/array
sayilar = [100,200,300,"Merhaba"]

print(sayilar)
#programcılar saymaya 0'dan başlar 
#index- indis => baslangıc değeri 0 
print(sayilar[0])
print(sayilar[3])
print(sayilar[-1]) #dizinin son indexini verir

sayilar.append(100) #listenin sonuna eleman ekler
print(sayilar)

sayilar.pop(2) #default olarak son indeximi siler
print(sayilar)

sayilar.remove(100) #pop'ın aksine indexe göre değil değere göre siler
print(sayilar)

sayilaraEkleme =  [1,2,3]
sayilar.extend(sayilaraEkleme) 
print(sayilar)

sayilar.append(sayilaraEkleme)
print(sayilar)
print(sayilar[6][2])

sayilar.clear() #dizinin içini boşaltan bi fonk
print(sayilar)


#karar yapıları
ortalamaNot = input("Lütfen ortalamanızı giriniz.")
#input => kullanıcıdan string bir değer alır
#string => int 

#type conversion
print(type(ortalamaNot))
ortalamNotAsInteger = int(ortalamaNot)
print(type(ortalamNotAsInteger))

if ortalamNotAsInteger >50 :
    print("Bravo")
#else if => elif 
elif ortalamNotAsInteger >40:
    print("Başarısız")
elif ortalamNotAsInteger >30:
    print("Başarısız")
else:
    print("Kaldınız")
    print("if blogundan bagımsız çalışıcak olan kısım")






















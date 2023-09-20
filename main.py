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
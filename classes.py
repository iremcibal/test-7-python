""" name = "irem"
number = 9
print(type(name))
print(type(number))

def age(age):
    return age
 """
#class nesne obje sınıf
class Human:
    #property , attribute => özellik nitelik
    #name = ""
    #age = 20

    def __init__(self,name,age):
        self.name=name
        self.age = age
        print("yapıcı blok çalıştı")

    #davranış,method
    def talk(self,message):
        print(message)

    def walk(self):
        print(f"{self.name} is walking..")

#instance üretmek - örneğini ürettik
#human1 = Human("irem",25) #constructor 
# human1.name = "irem"
# human1.age = 25
#human1.talk("Merhaba")
#human1.walk()
#self => içerisine yerleştirdiğim kalıp nesnenin kendisine işaret eden 
#classı temsil eden rezerve bir parametredir

#constructor => yapıcı blok nesne oluşturulduğunda ilk olarak bu yapı çalışır
#pythonda __init__()



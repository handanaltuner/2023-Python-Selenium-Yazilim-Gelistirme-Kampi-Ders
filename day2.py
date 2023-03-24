from human import Human
import matematik as math

math.bol(20,2)

faiz = 1.59
vade = "36"
KrediAdi = "ihtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(KrediAdi))

print(int(vade)+12)

#print(int(krediAdi))

faiz=str(faiz)
print(type(faiz))

vade =36 #input("Lütfen istediğiniz vade sayısını giriniz:")
print(type(vade))

vade = vade +12

#string interpolation
#Seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade : " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade : {vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade : {vade}")


isim="Handan" #input("İsminizi giriniz")
metin = "Merhaba {name}".format(name=123)
print(metin)

#f-string
metin = f"Hoşgeldiniz{isim}"
print(metin)

#listeler
#döngüler
#fonksiyonlar

krediler = ["ihtiyaç kredisi","Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) # length
#print(krediler[3]) = hata verir

dizi = ["ihtiyaç kredisi", 10, 5.2, True]

krediler.append("Özel Kredi")
print(krediler)

krediler.pop()
print(krediler)
krediler.append("Taşıt Kredisi")
krediler.remove("Taşıt Kredisi")
print(krediler)







krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)

# for
#i=0i<10

for i in range(10):
    print("xx")
    print(i)
print("***********************")
for i in range(5,10):
    print(i)
print("****************")
for i in range(0,51,10):
    print(i)
print("********************")
#for i in range(0.1,0.5):
 #   print(i)

krediler = ["ihtiyaç kredisi","Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("**********")
for i in range(len(krediler)):
    print(krediler[3])

for i in range(len(krediler)):
    print(krediler[i]) 
print("*************")

#sonsuz döngü
while i < 10:
    print("x")
    i += 1 
print("y")



while True:
    print("x")
    break


print("***Son döngü*****")

i= 0
while i < len(krediler):
    print(krediler[i])
    i+=1 
    if krediler[i] == "Konut Kredisi":
        break

#fonksiyonlar

fiyat = 100
indirim = 20
#definition define
def calculate():
    print(100-20)



def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)
def sayHello(name):
    print("Merhaba {name}")

calculate()
print(100-20)
calculateWithParams(50,10)
calculateWithParams(100,30)
    
calculate()
calculate()
calculate()
sayHello("Halit")
sayHello("Arif")
sayHello("Ayşe")

def calculateAndReturn(price, discount):
    return price-discount













print("**********************")
#fonk1 = calculatePrice(100,50)
#fonk2 = calculatePriceAndReturn(300,100)
#print(f"159.satır :{fonk1+100"}
#print(f"160.satır :{fonk2+100"}
print("**********")



#sınıflar =>classlar
#modules
#paket yonetimi


class Human:
    #built-in #constructor #initialize
    def __init__(self,name):
        self.name = name
        print("Bir human instance üretildi")
    def __str__(self):
       return f"STR Fonksiyonundan dönen değer: {self.name}"
    def talk(self,sentence): #self parametresi rezervli parametre
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking")

#instance => ornek
human1 = Human()
human1.name ="Enes"
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Halit")
human2.talk ("Selam")
human2.walk()
print(human2)

Human("Melike").talk("Merhaba")










print("kodlamaio")
baslik = "Taşıt Kredisi"
print("Taşıt Kredisi")
print(baslik)
#string => metinsel ifade
baslik="İhtiyaç Kredisi"
print(baslik)
#int, integer => tam sayı
vade = 36
ekVade =6
vade2="36"

#float, decimal,double
aylikOdeme=200.50

#bool, boolen => True veya False
yukselisteMi = False

#matematiksel operatörler

# + 
print(5+5)
print(vade + 12)
print(vade+ ekVade)

# - 
print(5-5)
print(vade-12)
print(vade - ekVade)
print(36-6)

# *
print(5*5)
print(vade  * 2 )
print(vade * ekVade)
print (10 * 10)

#  /
print(5/5)
print(vade / 2)
print(vade /ekVade)
print (10 /2)

yeniVade = vade /2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operatörü
print(10 % 2)
print(vade % 5 )
print(vade % ekVade)
print(30 % 10)

#mantiksal operatörler
print(1 == 1)
print (1 == 2)


#CTRL K + CTRL C kısayolu yorum satırı yapar
print(1 > 2)
print(3 > 1 )
print(1 > 1)
print(1 >=1 )

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1 != 1) #false döner
print(1 != 2) #true döner

# or and
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2 )
print(1 > 2 or 5 > 2 and 3 > 2 )

print(1 > 2 and 5 > 2 and 3 > 2 )

print(2 > 1 or 1 > 2 and 3 > 2)

#karar yapıları
#if else
sayi1= 10
sayi2 = 15

#sayi1 sayi2den büyükse ekrana sayi 1 daha büyük yazdır
#condition

#indent
if sayi1 < sayi2:
    print("sayi 1 sayi 2'den büyüktür")
    print("Hala if blogunun içerisindeyim")

#eğer if bloguna girmez ise
elif sayi1 == sayi2:
    print("iki sayı eşittir")
#eğer if ve else if bloklarında hiç birine girmiyorsa
else:
    print( "sayi 1 sayi 2den büyüktür")
print("Burası if blogu dışıdır")
#instance => ornek
from day2 import Human


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

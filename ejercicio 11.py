import datetime

h = datetime.date.today()

y = int(input("Introduce año (AAAA): "))
m = int(input("Introduce mes (MM): "))
d = int(input("Introduce dia (DD): "))

fecha = datetime.date(y, m, d)

dias = h - fecha

print("Dias transcurridos: ", dias.days)
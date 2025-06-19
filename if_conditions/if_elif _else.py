age = int(input('enter the age :-  '))

if (age <= 4):
    price=0
elif (age>4 and age<=18):
    price=25
else:
    price=40

print(f"u r price sir {price}")

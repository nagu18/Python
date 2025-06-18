x =10
while True:
    i = int(input('enter the value for gussing \n'))
    if i == x:
         print('u got it right')
         break
    elif i > 10:
         print('u guss to high')
    elif i < 10:
         print('u are close')


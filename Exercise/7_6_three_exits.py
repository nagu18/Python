'''
# break exit:- 
x =""
while True:
    x = int(input('enter the age:- '))
    if (x<3):
        print('ticket is free')
    elif (x>=3)and(x<=12):
        print("ticket is $10")
    elif (x>12):
        print('ticket is 15$')
    break # it break after excuting the break..
'''

#................................................................................
#condition exit:- 
'''
value =""
x=0
while (value.lower() != 'quit'): #using of condtion
    value = input("enter the value:- ")

    if value.lower() != 'quit':
        if value.isdigit(): #is digit is a function chek the is it a digit 
            x=int(value)
            if (x<3):
                print('ticket is free')
            elif (x>=3)and(x<=12):
                print("ticket is $10")
            elif (x>12):
                print('ticket is 15$')
'''


#flage variable:- 
'''
v = True
x=""
while v:
    x=input('enter the num,to exit the program write exit:- ')
    if x.lower() == 'exit':
        v = False
    if x.isdigit():
        x=int(x)
        if (x<3):
            print('ticket is free')
        elif (x>=3)and(x<=12):
            print("ticket is $10")
        elif (x>12):
            print('ticket is 15$')
    
'''
    

    

    
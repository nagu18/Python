login=['konda','admin']
pw=['1234','admin']
x = input('enter the user id:- ')
y = input('enter the password')
if login[0] == x and pw[0]==y or login[1]==x and pw[1]==y:
    print('u have login ')
else:
    print('u are not user u have been locked')
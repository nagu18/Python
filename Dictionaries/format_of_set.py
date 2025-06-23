lag = {'nagu':'telugu',
       'sabitha':'english',
       'konda':'japanies',}     # four spaces need to write in this formate
while True:
    key=input()
    value=input()
    lag[key]=value
    if key == 'break' and value == 'break':  #this is try of inputing by user by while loop
        break

del lag['break']
print(lag)

#input using while in set:
'''
lag = {'nagu':'telugu',
       'sabitha':'english',
       'konda':'japanies',}
while True:
    key=input()
    value=input()
    lag[key]=value
    if key == 'break' and value == 'break':
        break

del lag['break']
print(lag)
'''
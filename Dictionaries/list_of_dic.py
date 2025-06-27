

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(f'\nalien')


# adding many dic to list and print them as we can see
list=[]
for dic in range(2):
    info={'name':'nagendar','reg-no':'12314014','clg':'lpu'} #use any variable 
    list.append(info) #appended the info dic 2 times
print(list)
current_user = ['nagu18','konda@2004','nagu2004','nagendar2004','Konda']
newuser = ['Nagu18','kOnda@2004','love','amulya']
lower_current_user = [user.lower() for user in current_user]
for user in newuser:
    if user.lower() in lower_current_user:
        print(f'user {user} exit ')
    elif (user not in current_user):
        current_user.append(user)        
    
print(current_user)






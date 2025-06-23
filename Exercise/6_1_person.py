info ={'fist_name':'konda',
       'last_name':'nagendher',
       'age' : 21,
       'city':'uppal',
       }
x=input('enter the key to find the value:- ')
find_the_info=info.get(x,f'invalid key {x}')
print(find_the_info)

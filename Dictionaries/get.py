alean_0={'x_postion':0,'y_postion':25,'speed':'fast'}
#print(alean_0['points']) # we can see the key invalid error 
# we can use get method for error management:
x = input('enter key value to find:- ').strip()
find_the_key_value = alean_0.get(x,f'''error {x} key not exit's ''' )
print(find_the_key_value)
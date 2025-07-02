#while loop break if the while is true:-- 
msg=""
while msg != 'quit':   #condition is false it loops 
    msg = input('enter the msg:- ')
    if msg != 'quit':  # msg - here if not quit print the msg if quit it break the loop condition is true 
        print(msg)
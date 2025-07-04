while True:
    age_input = input('enter the age ,exit for quiting the program:- ')
    if age_input.lower() == 'exit':
        break    
    
    age = int(age_input)

    
    if (age) < 3:
        print('ticket is free')
    elif (age >= 3) and (age <=12) :
        print('ticket is 10$')
    elif (age > 12):
        print('ticket is 15$')
    
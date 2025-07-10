info ={}
flag = True
while (flag):
    name = input('enter the name:- ')
    mobile_num=input('enter the number:- ')
    info[name]=mobile_num
    x = input('if u want to add data  :- ')
    if x.lower().strip() == 'n' or x.lower().strip()=='no':
        flag=False

        print(f'this the data:- {info}')






#task3
#guest list for a party
#create a guest list
#remove gust who cancel the party
gust_num=int(input('enter the num u want to add :- '))
name = [input('enter the names:- ') for i in range(gust_num)]
print(name)

remove_names_num=int(input('enter the ppl num to remove:- '))
remove_values = [input('enter the name to remove:- ') for i in range(remove_names_num)]
for values_remove_name in remove_values:
    name.remove(values_remove_name)


print(name)


        

    
    

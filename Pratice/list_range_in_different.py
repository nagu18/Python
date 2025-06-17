#1 normal way --
sq=[]
list=list(range(1,11))
for value in list:
    sq.append(value**2)

print(sq)    

#2 compraensive way :- simpe hard to get  it ---
list_1=[v**2 for v in range(1,11)]
print(list_1)

#3 long way but clear way ---
list_2=[]
for value in range(1,11):
    sq_1=value**2
    list_2.append(sq_1)
print(list_2)




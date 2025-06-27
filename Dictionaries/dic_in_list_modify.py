names_list=[]
for names in range(10):
    n={'name':'nagu','age':'21','clg':'lpu'}
    names_list.append(n)

for name in names_list[:3]:
    if name['name'] == 'nagu':
        name['name']='konda'
        name['age']='22'
print(names_list)
        
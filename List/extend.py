#way to add list :- 

#type 1:
list1 = [1,2,3]
new_list=[4,5,6]
list1.extend(new_list)
print(list1)

#type 2:
new_1 = list([1,2,3])

new=[1,2,3]
for x in new:
    new_1.append(x)

print(new_1)
#type 3: 

x =[1,2,3]
y=[4,5,6]
add = x+y
print(add)

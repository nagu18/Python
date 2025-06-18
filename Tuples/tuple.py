tuple_list = (10,20,30)
# this is how to declare tuple
# tuple[0]=200 # can't not modify 
print(tuple[0])

#other way
new=tuple((1,2,3))
print(new)

#the
range_tuples=tuple((value**2 for value in range(1,10)))

print(range_tuples)
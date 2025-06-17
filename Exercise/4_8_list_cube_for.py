# takeing the elements for the list:-
cube=[1,2,3,4,5,6,7,8,9,10]
for c in cube:
    print(f"{c**3}")

print("\n")

# using list and range:-
cube_1=list(range(1,11))
for c_1 in cube_1:
    print(f"{c_1**3}")
print("\n")

# using list dicrect comprahensive :
cube_2=[value**3 for value in range(1,11)]
print(cube_2)
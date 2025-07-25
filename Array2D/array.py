array =[
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2],
]
guss = int(input('enter the value:- '))
for i in range(len(array)):
    for j in range(len(array[i])):
       if guss == array[i][j]:
           print(f'the index where we find the element:- {i},{j}')

array = [
    [2,3,4,5],
    [2,3,4,5],
    [2,3,4,5],
 ]
guess = int(input())
for i in range(len(array)):
    for j in range(len(array[i])):
        if guess == array[i][j]:
            print(f'{[i]}:{[j]}')
       

'''list=[x for x in range(1,10) if x%2 == 0]
print(list)
# [expression for item in iterable if condition]
#printing even num 
'''
list=[x for x in range(1,11)]
print(list)

'''
arr=[]
def even(x):
    arr.append(x)
    print(arr)
flag = True
while flag:
    x=int(input())
    if x%2==0:
        even(x)
    else:
        print(arr)
        flag=False
'''
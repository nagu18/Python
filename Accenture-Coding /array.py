'''Step 1: Find the two smallest elements in the array
	•	Array elements: 5, 2, 4, 3, 9, 7, 1
	•	Smallest element = 1
	•	Second smallest = 2

So the two smallest numbers are 1 and 2.

⸻

Step 2: Check their sum

1 + 2 = 3

Is 3 <= sum (9) ? ✅ Yes.

⸻

Step 3: Return their product

1 * 2 = 2

So, the output = 2.
'''
ans=[]
sum = 9  
arr = [5, 2, 4, 3, 9, 7, 1]  
n = 7
arr.sort()
if (arr[0]+arr[1])<9:
    print(arr[0]*arr[1])

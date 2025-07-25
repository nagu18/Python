
user_not_verify=['bhanu','mouli','sai','karthik']
user_verify=[]

while user_not_verify: #list variable name loop to end 
    current= user_not_verify.pop() #pop from last 
    print(f"the current user is adding to the list {current}")
    user_verify.append(current) # append current to user_verify list


for user_verifyed in user_verify:
    print(f'the verifed user : {user_verifyed}')

#list is emty
print(user_not_verify)

        
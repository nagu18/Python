
'''
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
If the list is empty, print the message We need to find some users!
Remove all of the usernames from your list, and make sure the correct message is printed.
'''

user_data = []
input_user='nagu'

if user_data:
    for user in user_data:
        if input_user in user:
            print(f"wecome user {input_user}")
        
else:
    print("We need to find some user")
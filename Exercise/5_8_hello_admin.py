'''5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. 
Imagine you are writing code that will print a greeting to each user after they log in to a website. 
Loop through the list, and print a greeting to each user.
If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.'''
# some advance that i know :-
login = input('enter the user name:- ').strip()
password = input('enter the user password:- ').strip()
user_info=('admin','nagu')
password_info=('admin','1234')
login_status = False
for user in user_info:
    for passw in password_info:
        if (login == user) and (password == passw):
            print(f"Hello {login}, thank you for logging in again.")
            login_status = True
            break

if login_status == False:
    print(f"invalid user:- {login}")

   
       


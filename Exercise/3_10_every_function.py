books = ['ccna-ed2-vo1','ccna-ed2-vol2','''hack-the-box-write-up's''','wazhu-doc']
lag_i_know=['english', 'telugu','hindi','jap-to-read-and-write-somewant','try to learn one more']
education=['ranker-e-techo', 'Siddhartha Institute of technology', 'lovely professional University','planning to abroad university']
skills = ['offensive thinking hacking', 'Kali Linux','ccna','seim','python','technical writing','C++','social engineering',]
games_i_played=['bgmi','lost of us']
game_i_not_played=[]
#-------------------this are the list now i will use i the function that i learn in it------------------------------------------------------
#modify
books[2]='''hack-the-box-doc's'''
print(f'hey i like to read a lot of books i will tell some of the books i am reading  {books[0]} which is the book on and i need to complete {books[1]} and {books[2]}')
#print the books on tem sorted fome to show in oder that book i will complet at last are sorted on first 
print(sorted(books,reverse=True))
#deleting an element :
del skills[6] # deleting the c++ due i have not praticeing daily like python...
print(f'i deleted a skill that i am not praticing daliy \n{skills}')
#remove an element when i know the element in list:
lag_i_know.remove('jap-to-read-and-write-somewant')
#insterting an element with the postion :
lag_i_know.insert(3,'jap-beginner-stage')
print(f'inserted an element\n{lag_i_know}')
#append to insert an element at last :
lag_i_know.append('Punjabi')
print(f'used append to insert an element at last \n{lag_i_know}')
#permenet sort :
education.sort(reverse=True)#sorting the education z to a 
print(education)
#using the pop :
not_played_game = games_i_played.pop(1)
game_i_not_played.append(not_played_game)
print(f'the game i played{games_i_played} and games i had not played {game_i_not_played}')
#using of len to konw the number of element :
num_of_education=len(education)
print(f'i did {num_of_education} educations')
#sorting the reverse the list perment  
skills.reverse()
print(skills)
#for tem sorting 
print(sorted(skills,reverse=True))#tem sorting not change in original list







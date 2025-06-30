pets=[]
#loops for adding dic in pets
for num in range(1):
    cat={'name':'chu',
         'type':'cat',
         'owner':'nagu'
     }
    dog={'name':'leo',
         "type":"dog",
     'owner':'mouli',
     }
    pets.append(cat)
    pets.append(dog)
#loop for pets nested for access in keys and values:
for  output in pets:
    [print('...........................................................')]
    for key,value in output.items():
        print(f'{key}:{value}')

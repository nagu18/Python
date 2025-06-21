# avalable toopings
toopings=list(['mushrooms', 'green peppers', 'extra cheese', 'olives'])
request=['mushrooms', 'french frie', 'extra cheese']
for req in request:
    if req in toopings:
        print(f"adding {req}")
    else:
        print(f"not avalable {req}")
# toopings can be a tuples 
# by using in to do list work like compare elemets etc...

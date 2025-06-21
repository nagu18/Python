# avalable toopings
toopings=list(['mushrooms', 'green peppers', 'extra cheese', 'olives'])
request=['mushrooms', 'french frie', 'extra cheese']
for req in request:
    if req in toopings:
        print(f"adding {req}")
    else:
        print(f"not avalable {req}")
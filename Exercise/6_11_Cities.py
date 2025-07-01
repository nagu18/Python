cities ={
    'TS':{
        'future-city':'#1',
        'hyderabad':'#2',
    },
    'AP':{
        'aparavathi':'#1',
    },
    'KN':{
        'beguluru':'#1',
    }
}
for key , value in cities.items():
    print(".......................................................................")
    print(f"state:- {key}")
    print('.......................................................................')
    for k,v in value.items():
        print(f"city:- {k} rank-{v}")
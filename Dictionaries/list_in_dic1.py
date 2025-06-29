fav_lag={'pawan':['java','cpp'],
         'adi':['cpp'],
         'mouli':['cpp','python'],
         'chaithanya':['python'],
         'bhanu':['python','cpp','java']
         }
for key,value in fav_lag.items():
    print(f"{key.title()}:______________________________")
    for v in value:
        print(f"\tthe fav lag: {v}")

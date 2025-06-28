fav_lag = {'adi':'cpp',
       'pawan':'java',
       'mouli':'cpp',
       'nagu':'python',
       }
list=['vikas','adi','pawan','bhanu' ]

#comrahensive list create of fav_lag.keys()
keys=[values for values in fav_lag.keys()] 


#loop the list with in and else 
for l in list:
    if l in keys:
        print(f'u alredy polled:- {l}\n')
    else:
        print(f"u should poll {l}")


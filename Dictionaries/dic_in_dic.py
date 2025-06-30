user = {'nagu':{
    'first':'konda',
    'last-name':'nagendar',
    'location':'ts',
},
'mouli':{
    'first':'mouli',
    'last-name':'bundi',
    'location':'ap',

}
}
# inner loop dic in dic using keys and values function:- 
for key ,value in user.items():
    print(f"{key}:- ")
    for k,v in value.items():
        print(f"{k}:{v}")
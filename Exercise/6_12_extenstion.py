#inner-loop and dic in dic , din in list,list in dic:
code = {'mouli':['java','cpp','python'],
        'vikas':['cpp','docker-file'],
        'bhanu':['python','dsa','cpp'],
        'nagu':['networking','python','bash','linux']
        }

skill_role={'vikas':{
    'skill':{
        'code':'cpp',
        'role':'DevOps'
    },
    'devops':{
        'manager-take':'chek the pipeline',
    },
},
'mouli':{
    'skill':{
        'code':'python-devloper',
        'role':'sde',
    },
    'sde':{
        'devloper':'devlop the aplication',
    },
},
}
#looping dic and value list :------
for k,v in code.items():
    print('.............................................')
    print(f'the {k}:- ')
    print(f"............................................")
    for value in v:
        print(f'the skills he have:{value}')

print('\n')

print('frinend how placed:--- ')
for kk,vv in skill_role.items():
    print('..............................................')
    print(f'the friend:- {kk.title()}')
    print('..............................................')
    for vv_key,vv_value in vv.items():
        print(f'{vv_key}:-')
        for vv_key2,vv_value2 in vv_value.items():
            print(f'the role he got:- {vv_key2} and work he do:- {vv_value2}')




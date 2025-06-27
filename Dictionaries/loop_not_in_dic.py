favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
notpool=['erin']
for name in favorite_languages.keys():
    print(name)

if name not in notpool:  #usig of not in as we can see 
    print(f"{notpool} is not pooled")
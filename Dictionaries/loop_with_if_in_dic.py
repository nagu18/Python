favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
cheker =['jen','edward']
for name in favorite_languages.keys():
    if name in cheker:
        print(f"{name} i see u love {favorite_languages[name]}")

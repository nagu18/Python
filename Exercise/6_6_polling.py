favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

list=['jen','sarah','mouli','vikas']
keys = [value for value in favorite_languages.keys()] #comprahensive will work not list(favorite_languages.keys()) 
for ppl in list:
    if ppl in keys:
        print(f'thank for pooling {ppl}')
    else:
        print(f'u are welcome for pooling {ppl}')
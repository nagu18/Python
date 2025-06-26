ppl = {}
while True:
    key = input('key: ')
    Value = input('value: ')
    ppl[key] = Value
    if key == 'done' and Value == 'done':
        del ppl['done']
        print(ppl)
        break
    




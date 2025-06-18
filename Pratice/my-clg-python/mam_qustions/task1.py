items = []

while True:
    enter = input("Enter a value (type 'done' to stop): ")
    if enter.lower() == 'done':
        break
    items.append(enter)

print("Final List:", items)


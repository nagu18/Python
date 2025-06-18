my_pizza = ['chikken pizza', 'veg pizza', 'garlick pizza']
my_friend_pizza = my_pizza[:]
ate = ['chikken chezz pizza', 'pie pizza', 'chilli chikken pizza']
for value_me in ate[0:2]:
    my_pizza.append(value_me)

print(my_pizza)
for value_friend in ate[2:]:
    my_friend_pizza.append(value_friend)

for my_values in my_pizza:
    print(f"my pizza :-  {my_values}")

print('\n')

for my_friend_values in my_friend_pizza:
    print(f"my friend pizza :-  {my_friend_values}")


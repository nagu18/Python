while True:
    topping = input("Enter a topping to add to your pizza (or type 'quit' to stop): ")
    if topping.lower() == 'quit':
        break
    print(f"I'll add {topping} to your pizza!")
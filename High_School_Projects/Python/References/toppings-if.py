requested_topping = ['mushrooms', 'extra cheese', 'green peppers']
for requested_tping in requested_topping:
    print("Adding " + requested_tping + ".")
    if requested_tping == 'green peppers':
        print("sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_tping + ".")

print("\nFinished making your pizza!")
#Checking to see if a slist is NOT empty.
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_tping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain Pizza?")
#Using multiple lists
available_toppings = ['mushrooms', 'extra cheese', 'green peppers', 'pepperoni', 'olives']
requested_toppings = ['mushrooms', ' pineapple', 'extra cheese', 'anchovies']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    elif requested_topping == 'pineapple':
        print("Gross. That's not a pizza topping.")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print('\nFinished making your pizza!')






#if requested_topping != 'anchovies':  # != Not equivalent to...
#   print("Hold the anchovies!")

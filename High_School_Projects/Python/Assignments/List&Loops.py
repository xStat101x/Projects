#4-1 Pizzas
pizzas = ['Cheese Pizza', 'Peporoni Pizza', 'Pinapple Pizza']

for pizza in pizzas:
    print(pizza)
    print("I like " + pizza)
print("I really like Pizza.")

#4-2 Animals
animals = ['dog', 'cat', 'fish']

for animal in animals:
    print(animal)
    print("A " + animal + "is a great pet.")
print("These animals all make great pets.")

#4-3 Counting to Twenty
for value in range (1,21):
    print(value)

#4-4 One Million
digits = range(1,1000001)
for digit in digits:
    print(digit)

#4-5 Summing a Million
digits = range(1,1000001)
minz = min(digits)
maxz = max(digits)
print(minz)
print(maxz)
sumz = sum(digits)
print(sumz)
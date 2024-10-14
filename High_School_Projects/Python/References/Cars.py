#Organizing lists
from audioop import reverse


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True) # apermantly sorted alphabetically in reverse
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() #permantly revers list
print(cars)
length = len(cars) #tells you the quanity of things in your list
print(length)
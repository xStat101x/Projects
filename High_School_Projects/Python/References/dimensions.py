#Tuples
dimensions = (200, 50)
print(dimensions[0]) 
print(dimensions[1])
#dimensions[0] = 250 --- won't work since you can't modify a tuple.
#something
for dimension in dimensions:
    print(dimension)
#can't modify a tuple, but you CAN redefine it
dimensions = (200, 50)
print("Original in dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print("\nModified dimentions:")
for dimension in dimensions:
    print(dimension)
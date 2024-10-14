age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65: #everyone normal aged
    price = 10
elif age >= 65:          #really REALLY old people
    price = 5
print("Your admissioon cost is $" + str(price) + ".")

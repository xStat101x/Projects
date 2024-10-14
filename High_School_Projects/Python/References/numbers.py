for value in range (1,6): #won't print final number
    print(value)
even_numbers = list(range(2,11,2))
print(even_numbers)
squares = []
for value in range (1,11):
    square = value**2
    squares.append(square)
    print(squares)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
minimumz = min(digits)
maximumz = max(digits)
sumz = sum(digits)
print(minimumz, maximumz, sumz)

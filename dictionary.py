squares ={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4))
print(squares)
print(squares.popitem())
print(squares)
squares.clear()
print(squares)
del squares
print (squares)

squares = {1: 1, 3: 9, 5: 25, 7 : 49, 9: 81}
for i in squares:
    print (squares[i])
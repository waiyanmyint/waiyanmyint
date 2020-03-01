Tuple.py

Tuple - ()

t = 12345, 54321, 'hello!'
t[0]

t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
t[0] = 88888


#but they can obtain mutable object
v = ([1, 2, 3], [3, 2, 1])
v

fruit = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruit[2:5])

#change Tuples Value

x = ("apple", "banana", "cherry", "orange")
y = list(x)
y[1] = "mango"
x = Tuple(y)
x

>>> Set

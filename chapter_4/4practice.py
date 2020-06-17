pizzas = ["pepperoni", "sausage", "cheese"]  # Pizzas
for pizza in pizzas:
	print(f"I like {pizza} pizza.")
print("I really love pizza!")  # Pizzas

animals = ["cat", "dog", "hamster"]
for animal in animals:
	print(f"I bet that a {animal} would make a great pet!")
print("Now that I think about it, any of these pets would be great!")  # Animals

numbers = list(range(1,21))  # Counting to Twenty
for value in numbers:
	print(value)

digits = [value for value in range(1,21)]
print(digits)  # These are two different methods to display digits 1 through 20, the first being separated, and the second in an inclusive list.

million = [value for value in range(1,1000001)] # The goal here is to print every value from 1 to 1,000,000, it's better to list comprehend this.

odds = list(range(1,21,2))  # Odd Numbers

threes = list(range(3,31,3))  # Threes
for three in threes:
	print(three)

cubes = []  # Cubes
for value in range(1,11):
	cube = value**3
	cubes.append(cube)
print(cubes)

cubec = [value**3 for value in range(1,11)]  # Cube Comprehension
print(cubec)  # Comprehension can save many lines of code, so it's always better to use if you can understand it.


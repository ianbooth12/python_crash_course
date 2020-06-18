pizzas = ["pepperoni", "sausage", "cheese"]  # Pizzas
for pizza in pizzas:
	print(f"I like {pizza} pizza.")
print("I really love pizza!")  # Pizzas

animals = ["cat", "dog", "hamster"]
for animal in animals:
	print(f"I bet that a {animal} would make a great pet!")
print("Now that I think about it, any of these pets are great!")  # Animals

numbers = list(range(1,21))  # Counting to Twenty
for value in numbers:
	print(value)

digits = [value for value in range(1,21)]
print(digits)  # Comprehensive lists can save lines of code

million = [value for value in range(1,1000001)]  # Comprehend larger lists

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
print(cubec)  # Comprehension can save many lines of code, use if comfortable

animals.append("tiger")
animals.append("horse")
print(animals)

print("The first animals I would think to adopt are:")  # Slices
print(animals[:3])
print("Three animals from the middle of my shortlist are:")
print(animals[1:4])
print(animals[2:])

friend_pizzas = pizzas[:]  # My pizzas, Your pizzas
friend_pizzas.append("sausage")
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)

my_foods = ["pizza", "chicken", "ice cream"]  # More Loops
friend_foods = my_foods[:]
my_foods.append("pasta")
friend_foods.append("popsicles")
print("My favorite foods are")
for food in my_foods:
	print(food)
print("My friend's favorite foods are:")
for food in friend_foods:
	print(food)

buffet_foods = ("wings", "chicken", "pizza", "cake", "bagels")  # Tuples
for food in buffet_foods:
	print(food)
buffet_foods = ("wings", "turkey", "pizza", "ice cream", "toast")
for food in buffet_foods:
	print(food)
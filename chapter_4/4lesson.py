bubs = ["kadin", "mason", "jad", "diego", "nicolas", "kavi", "ian"]
for bub in bubs:
	print(bub)
for bub in bubs: 
	print(f"We're planning dinner tonight, are you free, {bub.title()}?")
	print(f"{bub.title()} can't make it tonight, maybe we should reschedule.")
print("Thank you guys for all coming tonight!")

for value in range (1, 5):
	print(value)
for value in range (1, 6):
	print(value)  # Set the list 1 higher than your last value to include it

numbers = list(range(1, 10))
print(numbers)
even_numbers = list(range(2,11,2))  # The 3rd parameter sets the counting rule.
print(even_numbers)

squares = []
for value in range(1,11):
	square = value **2
	squares.append(square)  # This loop squares the given value and appends it.
print(squares)  # squares.append(value**2) can simplify this loop

integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Quick Commands for Data Lists
min(integers)  
max(integers)
sum(integers)  # In terminal, these calls return values from list

cubes = [value**3 for value in range(1,11,1)]  # List Comprehensions
print(cubes)  # Setting rules within the brackets can save lines over looping.

players = ["john", "tanner", "hadi", "kevin", "zach", "lucas"]  # Slicing a List
print(players[0:3])  # This will print values 0, 1, and 2.
print(players[2:7])  # Go one digit higher to include the last value.
print(players[:4])  
print(players[3:])  # Empty parameters will default to start or end of list.
print(players[-2:])  # Negative values move the slice in reverse order.

print("Here are 3 of the returning players on the team.")  # Looping Through a Slice
for player in players[:3]:
	print(player.title())

my_foods = ["pizza", "chicken", "ice cream"]  # Copying a List
friend_foods = my_foods[:]
print(f"My favorite foods are:") 
print(my_foods)
print(f"My friends' favorite foods are:\n{friend_foods}.") 

my_foods.append("pasta")
friend_foods.append("popsicles")
print(my_foods)
print(friend_foods)  # The lists with new information are still separate.

friend_foods = my_foods  # Listed below is a false method of copying lists.
friend_foods.append("eggs")
my_foods.append("toast")
print(friend_foods)
print(my_foods)  # This incorrect method makes two calls for one list

dimensions = (200, 50)  # Tuples (), are lists which can't be modified
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)  # Tuples work in loops the same way as lists.
dimensions = (400, 100)  # Tuples can only be redefined, not modified
print("New dimensions:")
for dimension in dimensions:
	print(dimension)

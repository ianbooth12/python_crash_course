bubs = ["kadin", "mason", "jad", "diego", "nicolas", "kavi", "ian"]
for bub in bubs:
	print(bub)
for bub in bubs: 
	print(f"We're planning dinner tonight, I hope you can make it, {bub.title()}!")
	print(f"Actually, it looks like {bub.title()} can't make it tonight, maybe we should reschedule.")
print("Thank you guys for all coming tonight!")  # Any commands in loops will all be executed before anything that follows the loop

for value in range (1, 5):
	print(value)
for value in range (1, 6):
	print(value)  # The range provided will not include the last digit, so to print 1-5, you must define a range of 1-6

numbers = list(range(1, 10))
print(numbers)
even_numbers = list(range(2,11,2))  # Adding a third parameter to the range will dictate how many digits to move by (Setting to 2 counts every other digit)
print(even_numbers)

squares = []
for value in range(1,11):
	square = value **2
	squares.append(square)  # This loop displays the squares of each value 1-10 by squaring the value within the loop and then appending it.
print(squares)  # The loop can be simplified by having one line within the loop, squares.append(value**2)

integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Quick Commands for Data Lists
min(integers)  
max(integers)
sum(integers)  # These commands, in a terminal command center, will yield different information about a numerical data list.

cubes = [value**3 for value in range(1,11,1)]  # List Comprehensions
print(cubes)  # By setting a rule within the list brackets, the results will automatically be appended to the list.

players = ["john", "tanner", "hadi", "kevin", "lucas"]  # Slicing a List
print(players[0:3])  # Because of Python's "stopping one short" rule, this will print terms 0, 1, and 2.
print(players[2:6])  # In order to include the last person in the list, use a number one higher than the last in the list.
print(players[:4])  
print(players[3:])  # Without a starting or ending parameter, the slice will start at the beginning or end of the list.


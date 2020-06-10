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
print(squares)
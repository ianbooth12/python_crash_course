car = 'tesla'  # Conditional Tests
print("Testing if car == tesla...")
if car == 'tesla':
	print("Yes, the car is a Tesla!")
else:
	print("The car is not a Tesla.")

car = 'bmw'
print("Testing if car == tesla...")
if car == 'tesla':
	print("Yes, the car is a Tesla!")
else:
	print("The car is not a Tesla.")

print("You must have a combined age of 50 to enter.")  # More Conditional Tests
ages = [24, 26, 19]
total_age = 0
for age in ages:
	total_age += age
if total_age >= 50:
	print("Alright, you guys can enter")
else:
	print("Sorry, but you guys can not enter")

usernames = ['Misterkadin11', 'barkbone', 'LEB97']  # Non case-sensitive test
for username in usernames:
	if username.lower() == 'misterkadin11':
		print("I invited you to the party, Kadin.")

print("You guys must be at least 17 to enter this movie.")  # Equality test
for age in ages:
	if age < 17:
		print("Sorry, you guys can't come in.")
else:
	print("Alright guys, you can come in!")

target_color = "green"  # Target Practice
if target_color == "green":
	print("You scored 5 points!")

target_color = "red"
if target_color == "green":
	print("That target is worth 5 points.")
elif target_color == "yellow":
	print("That target is worth 10 points.")
elif target_color == "red":
	print("That target is worth 15 points.")

age = 18
if age < 2:
	print("This is a baby.")  # Stages of Life
elif age < 4:
	print*("This child is a toddler.")
elif age < 13:
	print("This is a kid.")
elif age < 20:
	print("This person is a teenager.")
elif age < 65:
	print("This person is an adult.")


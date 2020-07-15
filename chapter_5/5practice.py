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

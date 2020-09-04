Ocars = ["tesla", "audi", "chevy", "ford"]  # A simple if statement
for car in cars:
	if car == "tesla":
		print(car.upper())
	else:
		print(car.title())  

cars[0] = "tesla"  # In CMD, this line will return "True" (Conditional Test)

requested_topping = "pepperoni"
if requested_topping != 'olives':  # The argument != checks for inequality.
	print("Hold the olives!")

age = 18
age == 18  # Numerical comparisons follow the same format.

answer = 42  # Example of checking a user's answer.
if answer != 17:
	print("Incorrect answer")

age = 18  # CMD arguments to check numerical values
age < 21  # TRUE
age <= 21  # TRUE
age > 25  # FALSE
age >= 18  # TRUE

age_0 = 20  # Checking multiple conditions with AND
age_1 = 16
if age_0 >= 18 and age_1 >= 18:  # Both must be true
	print("You guys can come in!")
else:
	print("Sorry, 18 or over only")

if age_0 >= 18 or age_1 >= 18:  # With "OR" only one must be true
	print("You have an adult, welcome in!")
else:
	print("Sorry, you need an adult")

requested_toppings = ["pepperoni", "olives", "peppers"]  # Checking list for a value
if 'sausage' in requested_toppings:
	print("Yes, you can get sausage")
else:
	print("Sorry, we don't have sausage.")

approved_members = ["jad", "denisse", "nicolas"]
member = 'kadin'

if member not in approved_members:
	print(f"Sorry, {member.title()}, but you're not on the list.")

age = 15  # Elif statements (Checking for 1 condition)
if age < 6:
	print("Your entry fee will be $5.")
elif age < 18:
	print("Your entry fee will be $8.")
elif age < 65:
	print('Your entry fee will be $15')
else:
	print("Your entry fee will be $10.")  # Last condition can be 'elif' or 'else'

if age < 6:
	price = 0
elif age < 18:
	price = 10
elif age < 65:
	price = 15
elif age >= 65:
	price = 10

print(f"Your price will be ${price}.")

requested_toppings = ["olives", "pepperoni"]
offered_toppings = ["olives", "pepperoni", "extra cheese"]
for topping in offered_toppings:
	if topping in requested_toppings:
		print(f"Adding {topping} to the pizza!")
print("The pizza is done!")

requested_toppings.insert(0,"peppers")
for topping in requested_toppings:
	if topping == "peppers":
		print(f"Sorry, we're out of {topping} right now.")
	else:
		print(f"Adding {topping} to the pizza...")
print("Your pizza is done!")

requested_toppings = []
if requested_toppings:  # This line checks if the list is not empty
	for topping in requested_toppings:
		print(f"Adding {topping}...")
else:
	print("Making one plain pizza...")

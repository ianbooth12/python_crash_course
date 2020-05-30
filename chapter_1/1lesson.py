message = "Hello Python World!"
print (message)

message = "Hello Python!"
print (message)  # Despite changing the value of message, the first printed message is the original, as print was requested before the change

name = "nore sheblack"
print(name.title())
print(name.upper())
print(name.lower())  # Printing with these commands give different results (See command prompt)

first_name = "ian"
last_name = "booth"
full_name = f"{first_name} {last_name}"
print(full_name)
print(full_name.title())
print(full_name.upper())

first_name = "nore"
last_name = "sheblack"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}.")
message = f"Hello, {full_name.title()}"
print(message)
print(message.upper())
print(message.lower())  # F strings are used to insert strings defined as variables into a larger string, which can then be defined as another variable, etc.

print("Kadin")
print("\tKadin")
print("Kadin\nJad\nMason")  # \t inserts a "tab" and \n inserts an indent

secret_note = "n\t\nu\to\tr"
print(secret_note)

favorite_food = "pizza "
print(favorite_food)
favorite_food.strip()
print(favorite_food)
print(f"My favorite food is {favorite_food.rstrip()}!")  # This only shows in terminal, but stripping white space changes resulting text


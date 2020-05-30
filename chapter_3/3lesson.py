bubitos = ["kadin", "mason", "ian", "jad", "kavi", "nicolas", "diego"]
print(bubitos[1])
print(bubitos[0])  # Lists are defined in brackets, and its contents can be called based on their placement, starting at 0
print(bubitos[3].title())
print(bubitos[5].upper())  # Capitalization commands learned before can also apply to strings pulled from a list

print(bubitos[-1])  # Calling the -1th term in the list will always call the last item

message = f"I think {bubitos[3].title()} is busy tonight, sadly"
print(message)  # Specific items in a list can be called in f strings, and modified with capitalizations.

foods = ["pizza", "apple", "carrot", "bacon"]
print(foods[1])
foods[1] = "cheese"
print(foods[1])  # Items in a list can be changed in the manner of changing a variable's value
foods.append("chicken")
print(foods)  # A new item can be added to a list using the append command
foods.insert(0, "pear")
print(foods)  # The insert command can add a new item at a specific point in the list
foods.insert(-1, "orange")  # Insert cannot use -1 to mean the end of the list like .append can

del(foods[0])
print(foods)
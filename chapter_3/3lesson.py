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
print(foods)  # "Del" command deletes an item from the list at the given index value

popped_food = foods.pop()
print(popped_food)
print(foods)  # The pop command will remove the last item from a list and allow it to be used later, for example as a variable value.

best_food = foods.pop(0)
print(best_food)  # A specific index value can also be popped if specified.

print(foods)
foods.remove("carrot")
print(foods)  # Using .remove on a list allows you to type the name of a specific item you wish to remove from the list.

fruit = "orange"
foods.remove(fruit)
print(foods)  # .remove also works if removing a string which is defined by a variable
print(f'{fruit.title()} is my favorite treat to go with a meal.')  # Once removed from the list, "orange" is still accessible through its variable, fruit.

cars = ["toyota", "mazda", "audi", "chevrolet", "bmw"]
print(cars)
cars.sort()
print(cars)  # Using the sort command puts the list in alphabetical order
cars.sort(reverse=True)
print(cars)  # Sorting with the reverse condition as true will sort to reverse alphabetical order

cars = ["toyota", "mazda", "audi", "chevrolet", "bmw"]
print("Listed below is the list in its original order")
print(cars)
print("Now the list will be temporarily sorted alphabetically")
print(sorted(cars))
print("The original format of the list will return now.")
print(cars)  # Using the "sorted" command rather than the sort modifier only temporarily changes the list sorting.

cars.reverse()
print(cars)
cars.reverse()
print(cars)  # The reverse MODIFIER doesn't sort to reverse alphabetic order, but simply reverses the order of the items.

print(cars)
len (cars)  # In a terminal command center, the argument lens will return the amount of items in the list.

print(cars[-1].upper())  # Often times, Python's index starting at 0 will throw people off when trying to call the last term, but using -1 simplifies this process.

bubitos = ["kadin", "mason", "ian", "jad", "kavi", "nicolas", "diego"]
print(bubitos[1])
print(bubitos[0])  # Lists are defined in brackets, labeled with positions(0,x)
print(bubitos[3].title())
print(bubitos[5].upper())  # Grammar modifiers can apply to list values

print(bubitos[-1])  # Calling the -1th term calls last term

message = f"I think {bubitos[3].title()} is busy tonight, sadly"
print(message)  # Specific items in a list can be called in f strings and modified.

foods = ["pizza", "apple", "carrot", "bacon"]
print(foods[1])
foods[1] = "cheese"
print(foods[1])  # Items in a list can be directly changed.
foods.append("chicken")
print(foods)  # A new item can be added to a list using the append command
foods.insert(0, "pear")
print(foods)  # The insert command can add a new item at a specific point in the list
foods.insert(-1, "orange")  # Insert cannot use -1 for end of list

del(foods[0])
print(foods)  # "Del" command deletes an item from the list at the given index value

popped_food = foods.pop()
print(popped_food)
print(foods)  # The pop command will remove the last item from a list by default.

best_food = foods.pop(0)
print(best_food)  # A specific index value can also be popped if specified.

print(foods)
foods.remove("carrot")
print(foods)  # Using .remove on a list allows you to remove an item by name.

fruit = "orange"
foods.remove(fruit)
print(foods)  # .remove also works if removing a string which is defined by a variable
print(f'{fruit.title()} goes great with a meal.')  # "orange" can still be called by var fruit

cars = ["toyota", "mazda", "audi", "chevrolet", "bmw"]
print(cars)
cars.sort()
print(cars)  # Using the sort modifier puts the list in alphabetical order
cars.sort(reverse=True)
print(cars)  # When reverse condition = true, sorts reverse alphabetical order

cars = ["toyota", "mazda", "audi", "chevrolet", "bmw"]
print("Listed below is the list in its original order")
print(cars)
print("Now the list will be temporarily sorted alphabetically")
print(sorted(cars))
print("The original format of the list will return now.")
print(cars)  # Using the "sorted" command changes the list sorting temporarily.

cars.reverse()
print(cars)
cars.reverse()
print(cars)  # The reverse MODIFIER flips the order values are returned in

print(cars)
len (cars)  # In terminal, the command "len" shows number of items in list

print(cars[-1].upper())  # Calling term -1 will call the last item in a list

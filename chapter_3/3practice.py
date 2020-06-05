invite_list = ["denzel", "kanye", "arnold"]  # Guest List

print(f"Unfortunately, {invite_list[1].title()} can't make it to dinner tonight")
invite_list.append("kelly")
invite_list.insert(1,"steve")
invite_list.remove("kanye")
print(invite_list)
print(f"Thank you {invite_list[0].title()} for your interest! Here is your invite to dinner")
print(f"Thank you {invite_list[1].title()} for your interest! Here is your invite to dinner")
print(f"Thank you {invite_list[2].title()} for your interest! Here is your invite to dinner")
print(f"Thank you {invite_list[3].title()} for your interest! Here is your invite to dinner")  # Changing Guest List

print("Good news! We've found a bigger dinner table so we can invite more people!")
invite_list.insert(0, "jay")
invite_list.insert(2, "kadin")
invite_list.append("kavi")
print(invite_list)
print(f"Thank you {invite_list[0].title()} for your interest! Here is your invite to dinner")
print(f"Thank you {invite_list[2].title()} for your interest! Here is your invite to dinner")
print(f"Thank you {invite_list[6].title()} for your interest! Here is your invite to dinner")  # More Guests

print("Sorry guests, but the table isn't here, so we only have room for two people!")
print(f"Sorry, {invite_list.pop(5).title()}, but we can't have you over any more.")
print(f"Sorry, {invite_list.pop(0).title()}, but we can't have you over any more.")
print(f"Sorry, {invite_list.pop(0).title()}, but we can't have you over any more.")
print(f"Sorry, {invite_list.pop(1).title()}, but we can't have you over any more.")
print(f"Sorry, {invite_list.pop(1).title()}, but we can't have you over any more.")
print(f"Good news, {invite_list[0].title()}, you're still good to come over!")
print(f"Good news, {invite_list[1].title()}, you're also invited!")
del invite_list[1]
del invite_list[0]
print(invite_list)  # Shrinking Guest List

locations = ["rome", "canada", "paris", "spain", "australia"]  # Seeing the World
print(locations)
print(sorted(locations))
print(locations)
print("Despite sorting the locations alphabetically, the original order of the items is retained")
print("The list will now be printed in reverse alphabetical order")
print(sorted(locations,reverse=True))
print("As shown below, the list is still in its original order despite our different sortings")
print(locations)
locations.reverse()
print(locations)
print("The list is now permanently reversed, but it can be changed back by repeating the command")
locations.reverse()
print(locations)
locations.sort()
print(locations)
print("The list is now printed in alphabetical order permanently, but it can be changed with another command")
locations.sort(reverse=True)
print(locations)  # Seeing the World

len(invite_list)  # (Dinner Guests) In terminal, this command would return a 0, as we emptied the guest list when working with it last

languages = ["english", "spanish", "french"]  # Every Function
languages.append("hebrew")
print(languages)
languages.insert(2,"german")
print(languages)
del languages[4]
print(languages)
languages.remove("german")
print(languages)
languages.pop(2)
print(languages)
first_language = "english"
languages.remove(first_language)
print(languages)
print(f"The first language I learned was {first_language.title()}.")
print(f"The second language I learned was {languages.pop(0).title()}.")  # Every Function
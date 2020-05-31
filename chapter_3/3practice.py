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
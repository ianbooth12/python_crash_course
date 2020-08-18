alien_0 = {'color': 'red' , 'points': 10}  # Format = {'key': value}

print(alien_0['color'])
print(alien_0['points'])  

player_score = 0
print(f"You hit the {alien_0['color']} alien! Adding your points...")
player_score += alien_0['points']
print(f"Your new score is {player_score}.")  # This sequence finds the color and adds the points.

alien_0['x_position'] = 0  # Adding data to existing dictionary
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}  # Starting with an empty dictionary

alien_1['color'] = "green"
alien_1['points'] = 5

print(alien_1)

alien_1['color'] = "blue"  # Modifying info
print(alien_1)

alien_0['speed'] = "fast"  # Determining movement speed

if alien_0['speed']  == "slow":
	x_movement = 1
elif alien_0['speed']  == "medium":
	x_movement = 2
elif alien_0['speed']  == "fast":
	x_movement = 3

alien_0['x_position'] += x_movement
print(f"The {alien_0['color']} alien moved to the side! It's now at {alien_0['x_position']}.")

del alien_0['speed']  # Deleting info from dictionary
print(alien_0)

favorite_languages = {  # Large dictionary entries
	'kadin': 'python',
	'jad': 'c++',
	'mathys': 'java',
	'kavi': 'c'
	}  # Entries separated by term if larger
print(favorite_languages)
print(f"Kavi's favorite coding language is {favorite_languages['kavi'].title()}")
print(f"Jad's favorite coding language is {favorite_languages['jad'].title()}.")

 # Asking for undefined variable will yield an error, below is the fix
speed_value = alien_0.get('speed', 'Speed not defined')
print(speed_value)

user_0 = {  # Looping through all k,v pairs
	'username': 'messxnger',
	'first_name': 'mason',
	'last_name': 'messenger'
}
for k, v in user_0.items():
	print(f"\nKey: {k}")
	print(f"Value: {v}")

for name, language in favorite_languages.items():  # Simplifying previous process
	print(f"\n{name.title()}'s favorite coding language is {language.title()}.")

for name in favorite_languages.keys():  # Looping all KEYS
	print(name.title())

friends = ['nicolas', 'kavi', 'kadin', 'jad']
for name in favorite_languages.keys():
	print(f"Hi, {name.title()}!")

	if name in friends:
		language = favorite_languages[name].title()
		print(f"Your favorite language is {language}, right?")

if 'mason' not in favorite_languages.keys():  # Checking for a Key
	print("Mason, what's your favorite coding language?")

for name in sorted(favorite_languages.keys()):  # Keys in Order
	print(f'Thanks for letting me know, {name.title()}!')

print("Below is a list of everyone's favorite languages.")
for v in favorite_languages.values():
	print(f"{v.title()}")

alien_2 = {
	'color': 'orange',
	'points': '20'
}

aliens = [alien_0, alien_1, alien_2]  # Nesting
for alien in aliens:
	print(alien)

aliens = []
  # Creating a list of duplicated aliens
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5}
	aliens.append(new_alien)
for alien in aliens[:5]:
	print(alien)
print(f"...")
  # Showing number of aliens
print(f"There are {len(alien)} aliens in the level right now.")

for alien in aliens[:4]:
	if alien["color"] == "green":
		alien ["color"] = "red"
		alien["points"] = 10
print(aliens[:5])

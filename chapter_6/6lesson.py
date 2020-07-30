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

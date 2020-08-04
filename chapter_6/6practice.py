kadin = {  # "Person"
'first_name': 'kadin',
 'last_name': 'rabo',
  'age': 18,
   'college': 'cal_poly'
   }

favorite_number = {  # Favorite Numbers
	'ian': 12,
	'kadin': 11,
	'jad': 1,
	'nicolas': 5,
	'mason': 88,
}

python_terms = {  # Glossary
	'tuples': 'Lists meant for permanent values',
	'if_statements': 'Tests for conditions in a list',
	'dictionaries': 'Used to store info within a key'
}
for key, value in python_terms.items():
	print(f"\nTerm: {key.title()}")
	print(f"Definition: {value.title()}")

rivers = {  # Rivers
	'hudson': 'united states',
	'nile': 'egypt',
	'amazon': 'brazil'
}
for river, country in rivers.items():
	print(f"\nThe {river.title()} river flows through {country.title()}.")
for river in rivers.keys():
	print(river)
for country in rivers.values():
	print(country)

poll_participants = ['mason', 'kavi', 'jad', 'nicolas', 'diego']
favorite_languages = {  # Polling
	'kadin': 'python',
	'jad': 'c++',
	'mathys': 'java',
	'kavi': 'c'
	}
for participant in poll_participants:
	if participant in favorite_languages.keys():
		print(f"Thanks for filling out the survey, {participant.title()}!")
	else:
		print(f"Could you please fill the survey, {participant.title()}?")


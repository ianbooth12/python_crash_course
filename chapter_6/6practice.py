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

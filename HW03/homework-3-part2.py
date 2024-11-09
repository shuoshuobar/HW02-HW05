# Yushuo Wang
# 2024-11-03
# Homework 3, Part 2

# SECTION 2.A: Lists
# Question 1: Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order
countries = ["United States", "China", "Japan", "Thailand", "Korea", "Russia", "France"]

# Question 2: Using a for loop, print each element of the list
for country in countries:
    print(country)

# Question 3: Sort the list permanently. 
countries = sorted(countries)
print(countries)

# Question 4: Display the first element of the list.
print(countries[3])

# Question 5: Display the second-to-last element of the list.
print(countries[-2]) 

# Question 6: Delete one of the countries from the list using its name.
countries.remove('Thailand')
print(countries)

# Question 7: Using a for loop, print each country's name in all caps.
for country in countries:
    print(country.upper())


# Section 2.B: Dictionaries
# Question 1: Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. 
# Pick a tree from:
# https://en.wikipedia.org/wiki/List_of_trees
tree = {'name': 'Sunland Baobab', 'species': 'Baobab', 'age': 1060, 'location_name': 'Limpopo Province, South Africa', 'latitude': -23.6211, 'longitude': 30.1981}

# Question 2: Print the sentence "{name} is a {years} year old tree that is in {location_name}"
print(tree['name'], "is a ", tree['age'], "year old tree that is in", tree['location_name'])

# Question 3: The coordinates of New York City are 40.7128° N, 74.0059° W. 
# Check to see if the tree is south of NYC, 
# and print "The tree {name} in {location} is south of NYC" if it is. 
# If it isn't, print "The tree {name} in {location} is north of NYC"
newyork_latitude = 40.7128
if tree['latitude'] > newyork_latitude:
    print("The tree", tree['name'], "is north of NYC")
else: 
    print("The tree", tree['name'], "is south of NYC")

# Question 4: Ask the user how old they are. 
# If they are older than the tree, display "you are {XXX} years older than {name}." 
# If they are younger than the tree, display "{name} was {XXX} years old when you were born."
age = input("How old are you? ")
age = int(age)
if age > tree['age']:
    age_difference = age - tree['age']
    print(f"You are {age_difference} years older than {tree['name']}.")
else: 
    age_difference = tree['age'] - age 
    print(f"{tree['name']} was {age_difference} years old when you were born.")


# Section 2.C: Dictionaries
# Question 1: Make a list of dictionaries of five places across the world - 
# (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. 
# Each dictionary should include each city's name and latitude/longitude (see note above).
# Source: Google - *coordinates of CITYNAME*
world = [ 
    {'name': 'Moscow', 'latitude': 55.7558, 'longitude': 37.6173},
    {'name': 'Tehran', 'latitude': 35.6892, 'longitude': 51.3890},
    {'name': 'Falkland Islands', 'latitude': -51.7963, 'longitude': -59.5236},
    {'name': 'Seoul', 'latitude': 37.5665, 'longitude': 126.9780},
    {'name': 'Santiago', 'latitude': -33.4489, 'longitude': -70.6693},   
    ]

# Question 2: Loop through the list, printing each city's name and whether it is above or below the equator 
# (How do you know? Think hard about the latitude.). 
# When you get to the Falkland Islands, also display the message 
# "The Falkland Islands are a biogeographical part of the mild Antarctic zone," 
# which is a sentence I stole from Wikipedia.
for city in world:
    if city['latitude']>0:
        print(f"{city['name']} is above the equator.")
    else: 
        print(f"{city['name']} is below the equator.")
    if city['name'] == "Falkland Islands":
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone.")

# Question 3: Loop through the list, printing whether each city is north of south of your tree from the previous section.
for city in world:
    if city['latitude']>tree['latitude']:
        print(f"{city['name']} is north of {tree['name']}.")
    else: 
        print(f"{city['name']} is south of {tree['name']}.")

# Yushuo Wang
# 2024-11-02
# Homework 3, Part 1

# SECTION 1.A: Lists
# Question 1: Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
list = [22, 90, 0, -10, 3, 22, 48]

# Question 2: Display the number of elements in the list.
print(len((list)))

# Question 3: Display the 4th element of this list.
print(list[3])

# Question 4: Display the sum of the 2nd and 4th element of the list.
sum_2nd_and_4th = list[1] + list[3]
print(sum_2nd_and_4th)

# Question 5: Display the 2nd-largest value in the list.
list_sorted = sorted(list)
print(list_sorted[-2])

# Question 6: Display the last element of the original unsorted list
print(list[6])

# Question 7: Display the sum of all of the numbers divided by two.
divided_value = sum(list)/2
print(divided_value)

# Question 8: Print whether the median or the mean of the numbers is higher
mean = sum(list)/len(list)
if len(list_sorted) % 2 == 1: # odd number of the list
    median = list_sorted[int(len(list_sorted)/2)]
else: median = (list_sorted[int(len(list_sorted)/2)] + list_sorted[int(len(list_sorted)/2 + 1)]) / 2
if mean > median:
    print("The mean is higher than the median.")
else: print("The median is higher than the mean.")


# Section 1.B: Dictionaries
# Question 1: Oftentimes dictionaries are used to describe multiple aspects of a single object. Like, say, a movie. 
# Define a dictionary called movie that works with the following code.
# print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])
movie = {'title': 'Wonder', 'year': '2017', 'director': 'Stephen Chbosky'}
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

# Question 2: On the lines after that, add keys to the movie dictionary for budget and revenue 
# (you'll use code like movie['budget'] = 1000), 
# and print out the difference between the two.
# Sources: 
# 1. https://www.imdb.com/title/tt2543472/
# 2. https://the-jh-movie-collection-official.fandom.com/wiki/Wonder_(film)#:~:text=It%20received%20positive%20reviews%20from,for%20Best%20Makeup%20and%20Hairstyling
movie = {'title': 'Wonder', 'year': '2017', 'director': 'Stephen Chbosky', 'budget': 20000000, 'revenue': 315000000}
difference = movie['revenue'] - movie['budget']
print(f"{difference:,}")

# Question 3: If the movie cost more to make than it made in theaters, print "That was a bad investment."
# If the film's revenue was more than five times the amount it cost to make, print "That was a great investment." 
# Otherwise print "That was an okay investment."
if movie['budget']>movie['revenue']:
    print("That was a bad investment.")
elif movie['budget']<movie['revenue']:
    print("That was a great investment.")
else:
    print("That was an okay investment.")

# Question 4: Sometimes dictionaries are used to describe the same aspects of many different objects. 
# Make ONE dictionary that describes the population of the boroughs of NYC. 
# Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. 
# (Tip: keeping it all in either millions or thousands is a good idea)
population = {'Manhattan': 1.6, 'Brooklyn': 2.6, 'Bronx': 1.4, 'Queens': 2.3, 'Staten Island': 0.47}

# Question 5: Display the population of Brooklyn.
print(population['Brooklyn'])

# Question 6: Display the combined population of all five boroughs.
total = population['Manhattan'] + population['Brooklyn'] + population['Bronx'] + population['Queens'] + population['Staten Island']
print(f"The total population of all five boroughs is {total} millions.")

# Question 7: Display what percent of NYC's population lives in Manhattan.
percent = population['Manhattan']/total
percent = (population['Manhattan']/total)*100
print(f"{percent:,.2f}%")
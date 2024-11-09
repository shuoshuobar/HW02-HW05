# Yushuo Wang
# 2024-10-29
# Homework 2

# Question 1: How old the user is
birth_year = int(input("What year were you born?"))
# Alternative way:
# year = input("What year were you born?")
# year = int (year)
age = 2024 - birth_year
print("You are " + str(age) + " years old.")

# Question 2: In that time, how many times the user's heart has beaten.
# Average heart rate (in beats per minute)
average_human_heart_rate = 80
minutes_lived = age * 365 * 24 * 60
total_human_heart_beat = minutes_lived * average_human_heart_rate
print("Your heart has beaten " + str(total_human_heart_beat) + " times.")

# Question 3: In that time, how many times a blue whale's heart has beaten.
average_whale_heart_beat = 6
total_whale_heart_beat = minutes_lived * average_whale_heart_beat
print("The blue whale's heart has beaten " + str(total_whale_heart_beat) + " times.")

# Question 4: In that time, how many times a rabbit's heart has beaten. 
# If the answer to rabbit heartbeats is more than a billion, 
# say "XXX billion" instead of the very long raw number
average_rabbit_heart_beat = 150
total_rabbit_heart_beat = minutes_lived * average_rabbit_heart_beat
print("The rabbit's heart has beaten " + str(total_rabbit_heart_beat/1000000000) + " billion times.")

# Question 5: Here are several ways to calculate and format/display numbers in Python 
# – string addition, f-strings, commas, etc etc etc. Redo one of the above questions above 
# with another technique and briefly explain the pros and cons of each approach.
# Redo Question 4:
print(f"The rabbit's heart has beaten {total_rabbit_heart_beat:,} times.") # Add Commas
print(f"The rabbit's heart has beaten {total_rabbit_heart_beat/1000000000:.3f} billion times.") # Keep three places
print(f"The rabbit's heart has beaten {total_rabbit_heart_beat/1000000000:.0f} billion times.") # Keep as an integer

# Question 6: Whether they are the same age as you, older or younger
# If older or younger, how many years difference
# If they were born in an even or odd year
my_age = 22
if age == my_age: 
    print("We are at the same age.")
elif age > my_age:
    print("You are older than me by " + str(age - my_age) + " years.")
else:
    print("You are younger than me by " + str(my_age - age) + " years.")
# Another way to do so: 
# elif age < my_age::
    # print("You are younger than me by " + str(my_age - age) + " years.")

if birth_year % 2 == 0:
    print("You were born in an even year.")
else:
    print("You were born in an odd year.")

# Question 7: How many times there has been a president from the Democratic Party in office 
# since they were born (1980 onward, and each president only counts once)
# List - For Loop - Count
democratic_presidents = [1980, 1992, 2008, 2020] # List
count=0
for year in democratic_presidents:
    if year>=birth_year:
        count+=1
print(f"Since you were born, there have been {count} different Democratic presidents in office.")

# Question 8: Which US President was in office when they were born (1980 onward)
if birth_year < 1981:
    president = "Jimmy Carter"
elif birth_year < 1989:
    president = "Ronald Reagan"
elif birth_year < 1993:
    president = "George H.W. Bush"
elif birth_year < 2001:
    president = "Bill Clinton"
elif birth_year < 2009:
    president = "George W. Bush"
elif birth_year < 2017:
    president = "Barack Obama"
elif birth_year < 2021:
    president = "Donald Trump"
else:
    president = "Joe Biden"
print(f"The U.S. President when you were born was {president}.")

# Question 9: Can you think of another approach to #7 and/or #8 that you could have tried? 
# Why is yours better? If you could not get #7/#8 to work, 
# use this question to explain what you were trying to do.
presidents = [
    ("Jimmy Carter", 1981),
    ("Ronald Reagan", 1989),
    ("George H.W. Bush", 1993),
    ("Bill Clinton", 2001),
    ("George W. Bush", 2009),
    ("Barack Obama", 2017),
    ("Donald Trump", 2021),
    ("Joe Biden", 2024)
]
for president, end_year in presidents:
    if birth_year < end_year:
        print(f"The U.S. President when you were born was {president}")
        break # When it finds a match, it prints the president's name and exits the loop using break. 
              # Or it would loop till the end to Joe Biden. 
# Why better: 
# Less Code: this approach avoids multiple elif statements, making the code shorter and more readable.

# Question 10: If someone says they were born in the future, 
# ask them for their year of birth again. Assume they'll do it right the second time.
# 教授标答：
birth_year = input("What year were you born? ")
birth_year = int(birth_year)

while birth_year > 2024: 
    print("This year is in the future. Please enter a valid year.")
    birth_year = int("What year were you born? ")
# Exercise  # 1
# Filter out all of the empty strings from the list below

places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']
# = [Argentina, San Diego, Boston, New York]

the_places = list(filter(lambda item: item.strip(), places))

print(the_places)
# HINT: LOOK FOR A STRING METHOD THAT REMOVES WHITESPACE


# Exercise  # 2
# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"
# # .sort(key=)

authors = ["Connor Milliken", "Victor aNisimov",
           "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]

authors.sort(key=lambda x: x.split()[-1])
print(authors)

# HINT: YOU'LL NEED TO CONVERT EACH PERSON'S NAME (A STRING) INTO A LIST IN ORDER TO GRAB THE LAST NAME BY
# THE INDEX


# Exercise  # 3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]

local_temp = list(map(lambda d: (d[0], d[1]*(9/5)+32), places))
print(local_temp)
# HINT: KEEP IN MIND PEMDAS. USE THE CELCIUS - FAHRENHEIT CONVERSION



# Exercise #4
# Write a recursive function to perform the fibonacci sequence up to the number passed in.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


#Testing
recur = 5

if recur <= 0:
    print ("Nope")
else:
    print("The Fibonacci (use this for your Renaissance paintings at your own risk")
    for i in range(recur):
        print(fibonacci(i))
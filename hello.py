import datetime as dt

name = input("Name: ")
birth_year = int(input("birth year: "))

this_year = dt.date.today().year
age = this_year - birth_year

#print ("Hello "+name+", you are " + str(age-1) + " years old")
print (f"Helo {name}, you are {age-1} or {age} years old")
import datetime as dt

name = input("Name: ")
birth_year = int(input("birth year:"))

this_year = dt.date.today().year
age = this_year - birth_year

print ("Hello "+name+", you are " + str(age) + " years old")
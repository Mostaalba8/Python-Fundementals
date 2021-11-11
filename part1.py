from datetime import date, datetime


name = "Mostafa"
birth_date = "8-August-1999"
print(birth_date)
date_to_int = datetime.strptime(birth_date, "%d-%B-%Y")
print(date_to_int)
age = date.today().year - date_to_int.year
print(age)
height = 180.33
siblings = 3
languages = ['Norwegian', 'English', 'Arabic']
male = True


from datetime import date, datetime


name = "Mostafa"
BIRTH_DATE = "8-August-1999"
print(BIRTH_DATE)
x = datetime.strptime(BIRTH_DATE, "%d-%B-%Y")
print(x)
age = date.today().year - x.year
print(age)
height = 180.33
siblings = 3
languages = ['Norwegian', 'English', 'Arabic']
male = True


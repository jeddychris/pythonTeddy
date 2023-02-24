from datetime import date
#extract today date
today = date.today()
input("Enter day of the week").lower()
if today.weekday() == date.today():
    print("true")
else:
    print("false")
if today.weekday() == 0:
    print("today is Monday")
elif today.weekday() == 1:
    print("Today is Tuesday")
elif today.weekday() == 2:
    print("Today is Wednesday")
elif today.weekday() ==3:
    print("Today is Thursday")
elif today.weekday() == 4:
    print("Today is Friday")
elif today.weekday() == 5:
    print("Today is Saturday")
else:
    print("Today is Sunday")


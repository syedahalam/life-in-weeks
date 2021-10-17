#your age
age = input("What is your current age?\n")
a = int(age)
print(f" - Your age in MONTHS is {a*12}\n - in WEEKS is {a*52}\n - and your age in DAYS is {a*365}\n")
years_left = 90-a
weeks_left = years_left*52
months_left = years_left*12
days_left = years_left*365
print(f"Your age is {a}\n\n If you are alive till 90 years\n - You have {years_left} YEARS,\n - {weeks_left} WEEKS,\n - {months_left} MONTHS,\n - {days_left} DAYS\n   left to LIVE 🤩 Have a very Happy Life ahead! 🤩 ")

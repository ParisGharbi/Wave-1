#Display the number of days in a month

#Read input from user
month = input("Enter the name of month: ")

#Compute the number of days in the month
days = 31
if month == "April" or month == "June" or \
    month == "September" or month =="November":
    days = 30
elif month == "February":
    days + "28 or 29"

#Display the result
print(month, "has", days, "days in it.")
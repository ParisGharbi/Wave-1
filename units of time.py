#Convert number of days, hours, minutes and seconds to seconds.

#Define constants
SECONDS_PER_MINUTE  = 60
SECONDS_PER_HOUR    = 3600
SECONDS_PER_DAY     = 86400
 
#Read inputs from user
days    = int(input("Enter number of Days: "))
hours   = int(input("Enter number of Hours: "))
minutes = int(input("Enter number of Minutes: "))
seconds = int(input("Enter number of Seconds: "))
 
#Calculate the days, hours, minutes and seconds
total_seconds = days * SECONDS_PER_DAY
total_seconds = total_seconds + ( hours * SECONDS_PER_HOUR)
total_seconds = total_seconds + ( minutes * SECONDS_PER_MINUTE)
total_seconds = total_seconds + seconds
 
#Display result
print("Total number of seconds: ","%d"%(total_seconds))

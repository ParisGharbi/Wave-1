#figure out the minimum collection of coins needed to represent a number of cents

CENTS_PER_TOONIE = 200
CENTS_PER_LOONIE = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5

#Read the number of cents from user
cents = int(input("Enter the number of cents: "))

#Determine the number of toonies by performing an interger division by 200
#Then compute the amount of change that still needs to be considered by computing the remainder after diving by 200

print(" ", cents // CENTS_PER_TOONIE, "toonies")
cents = cents % CENTS_PER_TOONIE

#Repeat process for loonies, quarters, dimes, and nickels
print(" ", cents // CENTS_PER_LOONIE, "loonies")
cents = cents % CENTS_PER_LOONIE

print(" ", cents // CENTS_PER_DIME, "dimes")
cents = cents % CENTS_PER_DIME

print(" ", cents // CENTS_PER_NICKEL, "nickels")

#Dispaly the number of pennies
print(" ", cents, "pennies")
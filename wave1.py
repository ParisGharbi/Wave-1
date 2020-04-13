def main():

	# ask input from user
	length = float(input("Enter the length of the field in feet: "))
	width = float(input("Enter the width of the field in feet: "))

	# converge area into acres
	acres = length * width / 43560

	# show the result
	print("The area of the field is", acres, "acres")

main()

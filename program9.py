#9.Write a Python program to convert height (in feet and inches) to centimeters. and vice versa. (depending on user input)
input_string = input("Enter inches and feet or centimeters of the distance ")
if input_string=='inches and feet':
	h_ft = int(input("Feet: "))
	h_inch = int(input("Inches: "))
	h_inch += h_ft * 12
	h_cm = round(h_inch * 2.54, 1)
	print("h_cm")
	
if input_string=='centimeters':
	centi=int(input("Centimeters: "))
	inch = 0.3937 * centi;
	feet = 0.0328 * centi;
	print("inches: ",inch)
	print("feet: ", feet)

#5.Write a Python program to convert the distance (in feet) to inches, yards, and miles.(depending on the user's choice)
d_ft = float(input("Enter the distance in feet"))
s_user = input("Enter inches,yards or miles ")
i_n='inches' 
m_i='miles'
y_a='yards'
if s_user==i_n :
	d_inches = d_ft * 12
	print("distance in inches=",d_inches)
if s_user==y_a :
	d_yards = d_ft / 3.0
	print("distance in yards=",d_yards)
if s_user==m_i :
	d_miles = d_ft / 5280.0
	print("distance in miles=",d_miless)

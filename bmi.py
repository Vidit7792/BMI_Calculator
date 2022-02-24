### INPUT

print "Enter height in feet and inches."

height_feet   = int(raw_input("Feet: "))
height_inches = int(raw_input("Inches: "))

total_height_inches = (height_feet * 12) + height_inches

print "Total height is {} inches.".format(total_height_inches)

weight_pounds = int(raw_input("Weight (pounds): "))


### BMI CALCULATION

bmi = float(weight_pounds * 703) / float(total_height_inches ** 2)
print "BMI: {:.2f}".format(bmi)


### BMI CLASSIFICATION

if bmi < 18.5:
  print "Underweight"
elif bmi >= 18.5 and bmi < 25.0:
  print "Normal weight"
elif bmi >= 25.0 and bmi < 30.0:
  print "Overweight"
else: # elif bmi >= 30
  print "Obese"


### COMPLEX COMPARISON

if bmi < 18.5:
  print "Underweight"
elif 18.5 <= bmi < 25.0:
  print "Normal weight"
elif 25.0 <= bmi < 30.0:
  print "Overweight"
elif bmi >= 30:
  print "Obese"

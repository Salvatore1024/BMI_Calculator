#BODY MASS INDEX CALCULATOR:

#Request from the user their weight in kg.
weight = float(input("Enter your weight in kg: "))

#Requet from the user their height in m.
height = float(input("Enter your height in m: "))

#Calculate the body mass index and store it in a variable "BMI".
BMI = weight / (height*height)

#Create a flow control structure that compares the "BMI" value with few
# numerical values, and print back the different BMI" values and statements
# results depending on which "if","elif","else" statement is true.
if BMI >= 30:
    print(f"Your BMI is equal to {BMI} and you are obese.")
elif BMI >= 25:
    print(f"Your BMI is equal to {BMI} and you are overweight.")
elif BMI >= 18.5:
    print(f"Your BMI is equal to {BMI} and you are normal.")
else:
    print(f"Your BMI is equal to {BMI} and you are underweight.")

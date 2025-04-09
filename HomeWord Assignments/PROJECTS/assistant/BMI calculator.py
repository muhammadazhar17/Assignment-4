import time
height = float(input("Enter your height in inches:"))
weight = float (input ("Enter your weight in lbs:"))
def  calculate_bmi(weight,height):

    """
    Calculate the Body Mass Index (BMI) based on weight and height."""
    # BMI = weight (kg) / (height (m) ** 2)
    bmi  = weight / (height ** 2)* 703
    if(bmi< 16):
        return 'severe thinness' ,bmi
    elif ( bmi >= 16 and bmi < 18.5) :
        return 'underweight',bmi

    elif (bmi >= 18.5 and bmi < 25):

        return 'healthy weight',bmi
    elif (bmi >= 25 and bmi < 30):
        return'overweight',bmi
    elif (bmi >= 30):
     return 'obese' .bmi
    quote, bmi = calculate_bmi (height, weight)
    print(f"Your BMI is: {bmi:.2f} and you are: {quote}")
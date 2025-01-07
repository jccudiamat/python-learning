#Bmi calculator
#Metric system and imperial

while True:

    try:

        underweight = 18.5
        normal = 25 
        overweight = 30
        classification = ""
        weight = 0
        height = 0
        bmi = 0

        metric_imperial = input("Enter Metric(m) or Imperial(i). Type (x) to exit: ")
        filtered = metric_imperial.strip().lower()

        if  filtered == "metric" or filtered == "m":
            weight = float(input("Enter weight in kilograms: "))
            height = float(input("Enter height meters: "))
            bmi = weight/(height**2)
        elif filtered == "imperial" or filtered == "i":
            weight = float(input("Enter weight in pounds: "))
            height = float(input("Enter height inches: "))
            bmi = (weight*703)/(height**2)
        elif filtered == "x":
            print("Goodbye!")
            break
        else:
            print("Invalid input!")
            continue
        
        if bmi <= underweight:
            classification = "You are underweight"
        elif bmi > underweight <= normal:
            classification = "You are normal"
        elif bmi > normal <= overweight:
            classification = "You are overweight"
        else:
            classification = "You are obese"
            
        print(f"Your BMI is: {bmi:.2f} \nClassification: {classification}")
        print()

    except ValueError:
        print("Invalid input")
        

    


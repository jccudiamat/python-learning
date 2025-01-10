#N = Population size
#e = Margin of error
#z = z-score
#p = standard deviation
#n = ? sample size

error_message =  "Please input numeric values only!"
border_message = "-"*30
#output_message = f"The sample size is {n:.2f}"

#Slovin's Formula function
#Sample size = N / (1+N*e^2)

def slovins_formula():
    try:
        print("SLOVIN'S FORMULA")
        N = int(input("N: "))
        e = float(input("e: "))
        n = N/(1+N*(e**2))
        print(f"The sample size is {n:.2f}")
    except ValueError:
        print(error_message)
        
#Very large population
#Sample size = ((z**2)*(p*(1-p)))/e**2
def unknown_very_large():
    try:
        print("UNKNOWN/VERY LARGE")
        z = float(input("z: "))
        e = float(input("e: "))
        p = float(input("p: "))
        n = ((z**2)*(p*(1-p)))/e**2
        print(f"The sample size is {n:.2f}")
    except ValueError:
        print(error_message)
#Standard formula
#Sample size = (((z**2)*p*(1-p))/e**2)/(1+((z**2)*p*(1-p))/(e**2*N))
def standard_formula():
    try:
        print("STANDARD FORMULA")
        N = int(input("N: "))
        z = float(input("z: "))
        e = float(input("e: "))
        p = float(input("p: "))
        n = (((z**2)*p*(1-p))/e**2)/(1+((z**2)*p*(1-p))/(e**2*N))
        print(f"The sample size is {n:.2f}")
    except ValueError:
        print(error_message)
#Quit program
def exit_program():
    print("Goodbye!")
    exit()

while True:
    try:
        formula = input("Standard Formula(sf)\nVery large population(up)\nSlovin's Formula(ss)\nEnter X to exit(x)\nChoose Formula: ").strip().lower()

        switcher = {

            'sf': lambda: standard_formula(),
            'up': lambda: unknown_very_large(),
            'ss': lambda: slovins_formula(),
            'x' : lambda: exit_program()
        }
        switcher.get(formula, lambda: print("Invalid choice!"))()
  
    except ValueError:
        print("Invalid Input!")
    print(border_message)
        

    
    
         


#break down currency to 1000, 500, 200, 100, 50, 20, 10, 5, 1
##while True:
##    try:
##        
##        money_rendered = int(input("Enter rendered amount: "))
##        remaining_amount = money_rendered
##        count_1000=0
##        count_500=0
##        count_200=0
##        count_100=0
##        count_50=0
##        count_20=0
##        count_10=0
##        count_5=0
##        count_1=0
##        
##        if money_rendered >= 1000:
##            count_1000 = money_rendered//1000
##            remaining_amount = money_rendered%1000
##        if 500 <= remaining_amount < 1000:
##            count_500 = remaining_amount//500
##            remaining_amount = remaining_amount%500
##        if 200 <= remaining_amount < 500:
##            count_200 = remaining_amount//200
##            remaining_amount = remaining_amount%200
##        if 100 <= remaining_amount < 200:
##            count_100 = remaining_amount//100
##            remaining_amount = remaining_amount%100
##        if 50 <= remaining_amount < 100:
##            count_50 = remaining_amount//50
##            remaining_amount = remaining_amount%50
##        if 20 <= remaining_amount < 50:
##            count_20 = remaining_amount//20
##            remaining_amount = remaining_amount%20
##        if 10 <= remaining_amount < 20:
##            count_10 = remaining_amount//10
##            remaining_amount = remaining_amount%10
##        if 5 <= remaining_amount < 10:
##            count_5 = remaining_amount//5
##            remaining_amount = remaining_amount%5
##        if 1 <= remaining_amount < 5:
##            count_1 = remaining_amount//1
##            remaining_amount = remaining_amount%1
##        if remaining_amount == 0:
##            print("1000: ", count_1000, "\n500: ", count_500, "\n200: ", count_200,"\n100: ",count_100, "\n50: ",
##                  count_50, "\n20: ", count_20, "\n10: ", count_10, "\n5: ", count_5, "\n1: ", count_1)
##        if money_rendered <0:
##            print("Don't be pessimistic!")
##    except ValueError:
##        print("Invalid input!")
##    print()


while True:
    try:
        money_rendered = int(input("Enter rendered amount: "))
        if money_rendered < 0:
            print("Don't be pessimistic!")
            continue

        # Define denominations
        denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
        counts = {}

        remaining_amount = money_rendered

        # Calculate counts for each denomination
        for denom in denominations:
            counts[denom] = remaining_amount // denom
            remaining_amount %= denom

        # Display results
        print("Breakdown:")
        for denom, count in counts.items():
            print(f"{denom}: {count}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
    print()


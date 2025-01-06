while True:
    try:
        sample_num = int(input("Enter number: "))
        if sample_num == 0:
            print("Cannot be zero")
        elif sample_num > 0:
            print(sample_num," is positive")
        else:
            print(sample_num," is negative")
    except ValueError:
        print("Type numbers only")
    print()

    

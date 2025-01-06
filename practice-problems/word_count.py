while True:

    #Count number of words
    sample_string = input("Enter Sample: ")
    arr_sample = sample_string.split(sep=" ", maxsplit=-1)
    word_count = len(arr_sample)

    #using for loop
    for i in arr_sample:
        if i == "":
            word_count -= 1
    print("Sample:",arr_sample,"\nWord count:",word_count)

    print()

    #using .pop()
    for j in arr_sample[:]:
        if j == "":
            arr_sample.pop(arr_sample.index(j))
    print("Sample:",arr_sample,"\nWord count:",len(arr_sample))

    print()

    repeat_program = input("Do you want to run the program again?(yes/no)").strip().lower()
    if repeat_program != "yes":
        print("Goodbye!")
        break

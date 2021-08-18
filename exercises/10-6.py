print("Enter 'q' at any time to quit.\n")
while True:
    try:
        a = input("The first num: ")
        if a == "q":
            break
        a = int(a)
        b = input("The second num: ")
        if b == "q":
            break
        b = int(b)
    except ValueError:
        print("You didn't enter a num")
    else:
        c = a+b
        print(f"The sum is {c}")
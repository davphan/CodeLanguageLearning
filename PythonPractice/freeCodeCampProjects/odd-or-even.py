replay = "y"
while (replay != "n"):
    answer = None
    while type(answer) != int:
        answer = input("What number are you thinking? ")
        try:
            answer = int(answer)
        except:
            print("Please enter an int value")
    if answer % 2 == 0:
        print("That's an even number!")
    else:
        print("That's an odd number!")
    replay = (input("Ask another number? (y/n) ")).lower()
    while replay != "y" and replay != "n":
        print("You entered: ", replay)
        replay = input("Please answer 'y' or 'n' ")
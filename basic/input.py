def right_or_left(way):
    print "You've chosen %s" % (way)
    print "pick up an option"
    answer = raw_input("Type yes or no to continue and hit 'Enter'").lower()
    if answer == "yes" or answer == "y":
        print "you chose to continue"
    elif answer == "no" or answer == "n":
        print "yo chose to go back"
    else:
        print " did not chose any valid option"

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
        right_or_left("left")
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
        right_or_left("right")
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

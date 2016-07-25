#Prompt for User Input
#Use an elif statement

Input= int(raw_input("What is Your Age?"))
if Input > 0:                                #check if the age is a valid number!
    if Input>30:
        print("You're too old for this!")
    elif Input>25:
        print("You're getting too old!")
    elif Input>18:
        print("You're just the right age!")
    else:
        print("You're too young!")
else:
    print("That's not a valid number")      #invalid age rejected!

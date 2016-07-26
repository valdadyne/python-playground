#Prompt for User Input
#Use an elif statement

Name = str(raw_input("What is Your Name?"))
Input = raw_input("What is Your Age?")
if Name != "" and isinstance(Input,int ):
    if Input > 0:                                #check for valid entries!
        if Input > 80:
            print(Name+" You're are an elder!")
        elif Input>30:
            print(Name+" You're too old for this!")
        elif Input>25:
            print(Name+" You're getting too old!")
        elif Input>18:
            print(Name+" You're just the right age!")
        else:
            print(Name+" You're too young!")

else:
    print("Invalid Entry!")         #invalid entries rejected!

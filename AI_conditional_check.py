x = str(input("Are You From Save In Your Brain Programming Class? Yes or No ?")).lower()
print(x)

if x == "yes":
    y = str(input("Which Class Are you from ? python or gaming class?")).lower()
        if y == "python":
                name = str(input("What is your name?")).title()
                print(name)
        elif y == "Gaming Class":
                name = str(input("What is your name")).title()
        else:
                print("Where are you from ?")
elif x == "no":
    y = str(input("Do You Want to join ?")).lower()
        if y == "yes":
            stdclass = str(input("Which class do you want study? We have python class and gaming clasee ")).lower()
                if stdclass == "python":
                    print("Very Well, I will arrange for You")
                else:
                    print("Very Well, I will arrange for you")
else:
    print("Have a nice day")



#    print("Do You Want to Join?")

"""
Program Goals:
1. Get input from user at multiple points
2. We need to covert some of the inputs to INTs from STRs
3. We need to provide choises
"""
myList = []

def mainProgram():
        while True:
            try:
                print("Hello there! Let's work with lists!")
                print("Choose from the following options. Type a number below!")
                choice = input("""1. add to a list
                2. Return the value at an index position!
                3. Random Search
                4. Exit program""")
                        if choice == "1":
                            addToList()
                        elif choice == "2":
                            indexVaules()
                        elif choice == "3":
                                randomSearch()
                        break
                except:
                        print("you made an oopsie doopsie"
        #add a way to loop action a way to quit 

def addToList():
        print("Adding to a list! Great choice!")
        newItem = input("Type an integer here!   ")
        myList.append (int (newItem))

def indexValues():
        print("Ooooooooooooh! I heard you need particular peice of data!")
        indexPos = input("What index position are you curious about?   ")
        print (myList[int(indexPos)])

if __name__ == "__main__":
    mainProgram()

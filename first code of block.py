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
                2. Add a bunch of numbers
                3. Return the value at an index position!
                4. Random Search
                5. Print contents of list
                6. Exit program""")
                        if choice == "1":
                            addToList()
                        elif choice == "2":
                            addABunch()
                        elif choice == "3":
                            indexVaules()
                        elif choice == "4":
                            indexVaules()
                        break
                except:
                        print("you made an oopsie doopsie"
        #add a way to loop action a way to quit 

def addToList():
        print("Adding to a list! Great choice!")
        newItem = input("Type an integer here!   ")
        myList.append (int (newItem))

def addABunch():
        print("something")
        numToAdd = input("something")
        numRange = input ("something")
        for x in range(0, int(numToAdd)):
                myList.Append(random.randit(0, int(numRange)))
        print("your list is now complete")

def indexValues():
        print("Ooooooooooooh! I heard you need particular peice of data!")
        indexPos = input("What index position are you curious about?   ")
        print (myList[int(indexPos)])

if __name__ == "__main__":
    mainProgram()

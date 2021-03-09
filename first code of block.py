"""
Program Goals:
1. Get input from user at multiple points
2. We need to covert some of the inputs to INTs from STRs
3. We need to provide choises
"""

def mainProgram():
        myList = []
        print("Hello there! Let's work with lists!")
        print("Choose from the following options. Type a number below!")
        choice = input("1. add to a list 2. Return the value at an index position!  ")
        if choice == "1":
            addToList()
        elif choice == "2":
            indexVaules()
        #add a way to loop action a way to quit 

def addToList():
        print("Adding to a list! Great choice!")
        newItem = input("Type an integer here!   ")
        myList.append (int (newItem))

def indexValues():

if __name__ == "__main__":
    mainProgram()

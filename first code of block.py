"""
Program Goals:
1. Get input from user at multiple points
2. We need to covert some of the inputs to INTs from STRs
3. We need to provide choises
"""
import random
myList = []
unique_list = []

def mainProgram():
        while True:
            try:
                print("Hello there! Let's work with lists!")
                print("Choose from the following options. Type a number below!")
                choice = input("""1. add to a list
                2. Add a bunch of numbers
                3. get an item from index
                4. sort list
                5. Random Search
                6. Linear Search
                7. reccursive binary search
                8. itarive binary search
                9. Print contents of list
                10. Exit program""")
                        if choice == "1":
                            addToList()
                        elif choice == "2":
                            addABunch()
                        elif choice == "3":
                            indexVaules()
                        elif choice == "4":
                            sortList(myList)
                        elif choice == "5"
                            randomSearch()
                        elif choice == "6":
                            linearSearch
                        elif choice == "7":
                            binSearch = input("what number do you want?   ")
                            recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearc))
                        elif choice == "8":
                            binSearch = input("what number do you want?   ")
                            result = iterativeBinarySearch(unique_list, int(binSearch))
                            if result != -1:
                                print("your number is at index position {}".format(result))
                            else:
                                print("your number is not found in that list"
                        elif choice == "9":
                            printLists()
                        else:
                            break
                except:
                    print("you made an oopsie doopsie"
        #add a way to loop action a way to quit 

def addToList():
        print("Adding to a list! Great choice!")
        newItem = input("Type an integer here!   ")
        myList.append(int(newItem))

def addABunch():
        print("we are going to add a bunch of numbers to the list")
        numToAdd = input("how many numbers would you like to add?   ")
        numRange = input ("and how high would you like these numbers to go?   ")
        for x in range(0, int(numToAdd)):
                myList.Append(random.randit(0, int(numRange)))
        print("your list is now complete")

def sortList(myList):
        for x in myList:
            if x not in unique_list:
                unique_list.append(x)
        unique_list.sort()
        showMe = input("Would you like to see the unique values in your list? Y/N   "
        if showMe.lower() == "y":
            print(unique_list)

def indexValues():
        print("At what index position do you want to search?")
        indexPos = input("What index position are you curious about?   ")
        print (myList[int(indexPos)])

def randomSearch():
    print("im random")
    print(myList[random.randit(0, len(myList)-1)])
    if len(unique_list) > 0:
        print(unique_list[random.randit(0, len(unique_list)-1)])

def linearSearch():
        print("we are gonna check each item one at a time, why have you made me do this?")
        searchItem = input("whaddya want?   ")
        for x in range (len(myList)):
            if myList [x] == int(searchItem):
                print("Your item is at index position {}" .format(x))

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("whic list do you want to see, sorted or un-sorted?  ")
        if whichOne.lower() == "sorted":
                print(unique_list)

def recursiveBinarySearch(unique_list, low, high, x):
        if high>= low:
            mid = (high + low) // 2

            if unique_List[mid] == x:
                print("your number is at index position {}".format(mid))
                return mid

            elif unique_list[mid] > x:
                    return recursiveBinarySearch(unique_list, low, mid - 1, x)

            else:
                return recursiveBinarySearch(unique_list, mid + 1, high,x)
        else:
            print("your number isnt here")

if __name__ == "__main__":
    mainProgram()

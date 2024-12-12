# Title: To create ADT that implements the "set" concept.
'''
Problem Statement: Implement all the functions of a dictionary (ADT) using hashing and handle collisions
using chaining with / without replacement. Data: Set of (key, value) pairs, Keys are mapped to values, Keys
must be comparable, Keys must be unique. Standard Operations: Insert(key, value), Find(key), Delete(key)
'''

setOne=[]
setTwo=[]

def addVal(Set):
# Function to add value to set
    val = int(input("Value to add:\t"))
    if (val in Set): # Checking if value already exists in set
        print(f"{val} already exists in the set.")
    else: # Adding value if does not exist
        Set.append(val)
    print(f"Set is:\t{Set}")
    
def delVal(Set):
# Function to delete value from set
    val = int(input("Value to remove:\t"))
    if(val not in Set): # Checking if value is not there in set
        print(f"{val} is not present in the set.")
    else: # Deleting value if it exists in set
        Set.remove(val)
    print(f"Set is:\t{Set}")

def searchVal(Set):
# Function to search value in set
    val = int(input("Value to search:\t"))
    if(val in Set): # Check if value is present in set
        print(f"{val} is present in the set.")
    else: # Print if value not present in set
        print(f"{val} is not present in the set.")

def size(Set):
# Function to print size (length) of set
    print(f"Size of set is:\t{len(Set)}")

def iterator(setA):
    a = iter(setA) # iter is a built-in function
    for i in  range(0,len(setA)-1):
        print(next(a),"->",end=' ')
    print(next(a))

def intersection(setA, setB):
# Function to perform intersection of two sets
    intersectionSet = []
    for i in setA:
        if i in setB:
            intersectionSet.append(i)
    print(f"Intersection is:\t{intersectionSet}")

def union(setA, setB):
# Function to perform union of two sets
    unionSet = []
    for i in setA:
        unionSet.append(i)
    for j in setB:
        if j not in setA:
            unionSet.append(j)
    print(f"Union is:\t{unionSet}")

def difference(setA, setB):
# Function to perform difference of two sets
    differenceSet = []
    for i in setA:
        if i not in setB:
            differenceSet.append(i)
    print(f"Difference is:\t{differenceSet}")

def subsetCheck(setA, setB):
# Function to check if two sets are subsets, called in subset()
    for i in setB:
        if i not in setA:
            return False
    return True

def subset(setA, setB):
# Function to print if two sets are subsets
    if subsetCheck(setA,setB):
        print("Set two is a subset of set one.")
    else:
        print("Set two is not a subset of set one.")

def main():
# Function for main menu
    while (True):
        print("--- MAIN MENU ---")
        print("1 -> Add value to set")
        print("2 -> Remove value from set")
        print("3 -> Search value in set")
        print("4 -> Show size of set")
        print("5 -> Iterate")
        print("6 -> Intersection of two sets")
        print("7 -> Union of two sets")
        print("8 -> Difference of two sets")
        print("9 -> Subset of two sets")
        print("10 -> Exit")
        optn = int(input("Choose an option (1-10):\t"))
        if (optn == 1):
            setSel = int(input("Which set to operate on?\n1. Set one\n2. Set two\nSet 1/2:\t"))
            total = int(input("Total values to add:\t"))
            for i in range(total):
                if (setSel == 1):
                    addVal(setOne)
                elif (setSel == 2):
                    addVal(setTwo)
                else:
                    print("\nPlease choose a valid option.\n")
        elif (optn == 2):
            setSel = int(input("Which set to operate on?\n1. Set one\n2. Set two\nSet 1/2:\t"))
            if (setSel == 1):
                delVal(setOne)
            elif (setSel == 2):
                delVal(setTwo)
            else:
                print("\nPlease choose a valid option.\n")
        elif (optn == 3):
            setSel = int(input("Which set to operate on?\n1. Set one\n2. Set two\nSet 1/2:\t"))
            if (setSel == 1):
                searchVal(setOne)
            elif (setSel == 2):
                searchVal(setTwo)
            else:
                print("\nPlease choose a valid option.\n")
        elif (optn == 4):
            setSel = int(input("Which set to operate on?\n1. Set one\n2. Set two\nSet 1/2:\t"))
            if (setSel == 1):
                size(setOne)
            elif (setSel == 2):
                size(setTwo)
            else:
                print("\nPlease choose a valid option.\n")
        elif (optn == 5):
            setSel = int(input("Which set to operate on?\n1. Set one\n2. Set two\nSet 1/2:\t"))
            a = None
            if (setSel == 1):
                iterator(setOne)
            elif (setSel == 2):
                iterator(setTwo)
            else:
                print("\nPlease choose a valid option.\n")
        elif (optn == 6):
            intersection(setOne, setTwo)
        elif (optn == 7):
            union(setOne, setTwo)
        elif (optn == 8):
            difference(setOne, setTwo)
        elif (optn == 9):
            subset(setOne, setTwo)
        elif (optn == 10):
            print("\n\n## END OF CODE\n\n")
            exit(1)
        else:
            print("Please choose a valid option (1-10).")

main() 
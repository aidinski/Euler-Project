#!/usr/bin/python
from decimal import *
import csv
import difflib

def count (enteredString, sanctionedString, desiredPercentage):
    similarChar = 0

    for parsingChar in enteredString:
        if sanctionedString.find(parsingChar)>=0:
            similarChar +=1

    enteredStringLength = len(enteredString)
    differencePercentage = ((similarChar / Decimal(enteredStringLength))*100)

    
    if differencePercentage >= Decimal(desiredPercentage):
        return 'isInTheList'

def similarity (enteredString, sanctionedString, desiredPercentage):
    stringSimilarity = difflib.SequenceMatcher(None, enteredString, sanctionedString).ratio()
    if stringSimilarity >= (Decimal(desiredPercentage)/100):
        return 'isInTheList'
    else:
        return False
    

def readFromCVE(fileName):
    #prompt the user for a file to import
    listName = open(fileName, 'r')
    if not listName: return

    reader = csv.reader(listName, delimiter=',')
    listNameArray = list(reader)
    return (listNameArray)

# Main Function
def main():
    filename = input ("Sanction list: ")
    desiredPercentage = input ("Percentage Change 1-100: ")
    sanctionedListArray = readFromCVE(filename)
    indicator = 0
    while True:
        enteredString = input ("Name: ")       
        for parsingName in sanctionedListArray[0]:
            #flag = count (enteredString.upper(), parsingName.upper(), desiredPercentage)
            flag = similarity (enteredString.upper(), parsingName.upper(), desiredPercentage)
            if flag == 'isInTheList':
                indicator += 1

        if indicator > 0:
            print (enteredString, 'is in the sanction list')
        else:
            print (enteredString, 'is NOT in the sanction list')
        indicator = 0

# Driver Code
if __name__ =="__main__":
    main()
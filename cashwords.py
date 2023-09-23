wordList = []
letterList = []
computedList = []

def wordCash(word, letterList):
    letterPosition = 0
    if word[letterPosition] in letterList:
        if wordCashHelper(word, letterList, letterPosition+1) == True:
            return word
        else:
            return None
    return None

def wordCashHelper(word, letterList, letterPosition):
    if word[letterPosition] in letterList:
        if letterPosition + 1 == len(word):
            computedList.append(word)
            return True
        wordCashHelper(word, letterList, letterPosition+1)
    return False

def listMaker(list,n):
    for i in range(1,int(n)):
        word = input(f"{i}: ")
        if (word == "**"):
            break
        else:
            list.append(word)
    corrections = input("Do you need to make any corrections? [y/n]: ")


    while (corrections == "y"):
        index = input("Enter the index for correction: ")
        list[int(index) - 1] = input(f"New enter the correction for index {index}: ")
        for i in range(18):
            print(f"{i+1}: {list[i]}")
        corrections = input("Correction made, do you need to make addictional corrections? [y/n]: ")
    ##make corrections
    print()

def main():
    print("Cashwords puzzle solver loaded...")
    print("You will have to enter all the words and letters one by one...")
    print("If you made a typo, you can make corrections after finish entering...")
    print("When you finish entering the last word, enter ** to escape from word entering")
    print("Enter the words:")
    listMaker(wordList,25)
    print("Now enter the letter: ")
    listMaker(letterList,19)
    for word in wordList:
        wordCash(word,letterList)
    print(f'Found {len(computedList)} words: {computedList}')


main()
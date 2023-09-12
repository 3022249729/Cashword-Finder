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




print("Cashwords puzzle solver loaded, enter all the puzzle words:")
for i in range(1,19):
    wordList.append(input(f"{i}: "))
print("Now enter the the letters: ")
for i in range(1,19):
    letterList.append(input(f"{i}: "))
#Expected length 18 for both


if (len(wordList) != 18):
    print("Word list length error")
elif (len(letterList) != 18):
    print("Letter list length error")
else:
    for word in wordList:
        wordCash(word,letterList)
    print(f'Found {len(computedList)} words: {computedList}')

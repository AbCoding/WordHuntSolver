import itertools
import WordChecker
ListOfWords=[]
for i in range(3, 16):
    word = WordChecker.GenerateListFromFile("output_" + str(i) + ".txt")
    ListOfWords.append(word)
def CheckAllWords(letters):
    for i in range(3,len(letters)+1):
        print(checkNletterWords(letters,i))
    return 1


def checkNletterWords(letters, n):
    possibleWords = list(itertools.permutations(letters, n))
    words=[]
    for i in possibleWords:
        st= ""
        for j in i:
            st +=j
        if st not in words:
            words.append(st)
    out= []
    for i in words:
        if i in ListOfWords[n-3]:
            out.append(i)
    return out


letters=["a","b","c","d","e","f","g","h"]
CheckAllWords(letters)

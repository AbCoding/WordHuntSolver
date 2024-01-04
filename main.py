import WordChecker
import WordHuntMatrixTraverser
import MatrixGen
import  GetWordHuntPoints
def sort_strings_by_length(strings):
    # Sort the list of strings based on their length in descending order
    sorted_strings = sorted(strings, key=len, reverse=True)
    return sorted_strings


ListOfWords = []
wordset= WordChecker.GenerateListFromFile("Words.txt")
for i in range(3, 16):
    word = WordChecker.GenerateListFromFile("output_" + str(i) + ".txt")
    ListOfWords.append(word)


matrix = [
    ["o", "a", "t", "r"],
    ["i", "h", "p", "s"],
    ["h", "t", "n", "r"],
    ["e", "n", "e", "i"]
]

matrix=MatrixGen.create_matrix()

generated_words = WordHuntMatrixTraverser.generate_words(matrix,wordset)


out=[]
for i in generated_words:
    word_length = len(i)
    if word_length > 2 and word_length < 16:
        if i in ListOfWords[word_length - 3]:
            out.append(i)



print(len(out))
print(GetWordHuntPoints.GetTotalScore(out))
print(sort_strings_by_length(out))
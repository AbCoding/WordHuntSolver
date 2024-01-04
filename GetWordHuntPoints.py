def getPoint(word):
    if len(word)==3:
        return 100
    elif len(word)==4:
        return 400
    elif len(word) == 5:
        return 800
    elif len(word) == 6:
        return 1400
    elif len(word) == 7:
        return 1800
    elif len(word) == 8:
        return 2200
    elif len(word)==9:
        return 2600
    elif len(word)==10:
        return 3000
def GetTotalScore(listOfWords):
    s=0
    for i in listOfWords:
        s+=getPoint(i)
    return  s
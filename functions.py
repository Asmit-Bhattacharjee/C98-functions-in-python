def countingWordsFromFile():
    filePath = input("Enter the file path: ")
    numberOfWords = 0
    file = open(filePath, 'r')
    for line in file:
        words = line.split()
        numberOfWords=numberOfWords+len(words)
    print("Number of Words in the file is: ", numberOfWords)

countingWordsFromFile()
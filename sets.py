def words(wordList):
    uniqueList = set()
    duplicateList = set()

    for word in wordList:
        if word in uniqueList:
            duplicateList.add(word)
        uniqueList.add(word)

    return uniqueList, duplicateList

unique, duplicate = words(["banana", "banana", "orange", "apple", "cherry", "pear", "cherry"])

print("Unique Words: ", unique)
print("Words that appear more than once: ", duplicate)
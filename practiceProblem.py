def binAvailable(N,M,C,I):
    for i in range(0, N):
        if I[i] > C[i] * M:
            return "NO"
        
    return "YES"

print(binAvailable(3,2,[2,3,1],[4,5,2]))

import re

def validLicense(plate):
    pattern = r'^[A-Z]{1,3}[0-9]{4}[A-Z]{0,2}$'
    result = re.search(pattern, plate)
    if result:
        return "VALID"
    else:
        return "INVALID"

print(validLicense('ABC1234'))
print(validLicense('A1234BCD'))
print(validLicense('AB12345'))
print(validLicense('ABC1234Z'))

pattern = r'(^.).*\1$'
print(re.search(pattern, "bqwwtbab"))

def countWords(text, ignoreList):
    wordList = re.findall(r'\b\w+\b', text)
    ignoreListUpper = [x.upper() for x in ignoreList]
    wordList = [x for x in wordList if x.upper() not in ignoreListUpper]

    frequencyList = [0] * len(wordList)
    uniqueWords = set()
    for i in range(0, len(wordList)):
        if wordList[i] in uniqueWords:
            frequencyList[i] += 1
            print(frequencyList)
        else:
            uniqueWords.add(wordList[i])

    return len(uniqueWords), wordList[frequencyList.index(max(frequencyList))]

print(countWords("The quick brown fox jumps over the lazy dog. The dog barks.", ["the", "a"]))

text = "banana split"
print([x for x in text if x in ['a', 'i']])

def reverseVowels(s):
    vowels = [x for x in s if x in ['a', 'i', 'e', 'o', 'u']]
    vowels.reverse()
    
    index = 0
    result = []
    for char in s:
        if char in vowels:
            result.append(vowels[index])
            index+=1
        else:
            result.append(char)
    
    return ''.join(result)

print(reverseVowels("hello"))
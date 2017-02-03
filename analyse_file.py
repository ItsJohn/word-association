from db import find_this_file


def openFile(filename, index, stopWords):
    data = find_this_file(filename, stopWords)
    return getScore(index, data)


def getScore(position, data):
    words = []
    for word in data:
        associations = word['associations']
        if type(associations) is list:
            word['score'] = int(list(associations[position].values())[0]) * word['frequency']
        else:
            word['score'] = 0
        words.append(word)
    return words

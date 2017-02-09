from db import find_this_file


def openFile(filename: str, index: int, stopWords: bool):
    data = find_this_file(filename, stopWords)
    return getScore(index, data)


def getScore(position: int, data: list):
    words = []
    for word in data:
        associations = word['associations']
        if type(associations) is list:
            word['score'] = int(list(
                associations[position].values())[0]
            ) * word['frequency']
        else:
            word['score'] = 0
        words.append(word)
    return words

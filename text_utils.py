from string import punctuation
from collections import Counter
import json


def remove_punctuation(words):
    new_words = []
    for word in words:
        front = False
        back = False
        if word in punctuation:
            word = ""
        else:
            while ((front is False) or (back is False)) and word is not "":
                if front is False:
                    if word[:1] in punctuation:
                        word = word.replace(word[:1], "")
                    else:
                        front = True
                if back is False:
                    if word[-1:] in punctuation:
                        word = word.replace(word[-1:], "")
                    else:
                        back = True
        if word is not "":
            new_words.append(word)
    return new_words


def get_word_associations():
    with open('ea-thesaurus-lower.json') as normsf:
        norms = json.load(normsf)
    return norms


def generate_structured_data(data, frequency_count):
    words = []
    norms = get_word_associations()
    for word in data:
        associations = {}
        if word in norms.keys():
            associations = {
                'word': word,
                'frequency': frequency_count[word],
                'associations': norms[word][:3]
            }
        else:
            associations = {
                'word': word,
                'frequency': frequency_count[word],
                'associations': 'was not found in the associations list'
            }
        words.append(associations)
    return words


def manipulate_data(data):
    data = data.split(' ')
    data = remove_punctuation(data)
    frequency_count = Counter(data)

    data = set(data)
    return generate_structured_data(data, frequency_count)


def read_file(filename):
    doc = ''
    with open(filename, encoding="latin-1") as fh:
        for line in fh:
            doc += line[:-1].lower() + ' '
    return doc

from string import punctuation
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from operator import itemgetter
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
                        word = word[1:]
                    else:
                        front = True
                if back is False:
                    if word[-1:] in punctuation:
                        word = word[:-1]
                    else:
                        back = True
        if word is not "":
            new_words.append(word)
    return new_words


def get_word_associations():
    with open('ea-thesaurus-lower.json') as normsf:
        norms = json.load(normsf)
    return norms


def sortvalues(data):
    return int(list(data.values())[0])


def generate_structured_data(data, frequency_count):
    words = []
    norms = get_word_associations()
    for word in data:
        associations = {}
        if word in norms.keys():
            associations = {
                'word': word,
                'frequency': frequency_count[word],
                'associations': sorted(
                    norms[word][:3],
                    key=sortvalues,
                    reverse=True
                )
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
    data = word_tokenize(data)
    data = remove_punctuation(data)
    frequency_count = Counter(data)

    return generate_structured_data(set(data), frequency_count)


def read_file(filename):
    doc = ''
    with open(filename, encoding="latin-1") as fh:
        for line in fh:
            doc += line[:-1].lower() + ' '
    return doc


def removeStopWords(data):
    new_words = []
    for word in data:
        if word['word'] not in stopwords.words('english'):
            new_words.append(word)
    return new_words

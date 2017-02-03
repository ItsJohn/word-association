import pymongo
import hashlib
from os import stat
from text_utils import read_file, manipulate_data


client = pymongo.MongoClient()
db = client['wordAssociationDB']


def find_this_file(filename):
    data = read_file(filename)
    hash_details = hashlib.sha256(bytes(data, encoding='utf-8')).hexdigest()
    collections = db[hash_details]
    if hash_details in db.collection_names():
        data = list(collections.find())
    else:
        data = manipulate_data(data)
        for value in data:
            collections.insert(value, check_keys=False)
    return data

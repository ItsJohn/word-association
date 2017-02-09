import pymongo
import hashlib
from os import stat
from text_utils import read_file, manipulate_data, removeStopWords


client = pymongo.MongoClient()
db = client['wordAssociationDB']
collections = db['files']


def find_this_file(filename: str, stopWords: bool):
    file_contents = read_file(filename)
    hash_details = hashlib.sha256(
        bytes(
            file_contents,
            encoding='utf-8'
        )
    ).hexdigest()
    data = collections.find_one({
        hash_details: {
            '$exists': True
        }
    }, {
        '_id': False
    })
    if not data:
        data = manipulate_data(file_contents)
        data = {hash_details: data}
        collections.insert(data, check_keys=False)
    if stopWords:
        return removeStopWords(data[hash_details])
    return data[hash_details]

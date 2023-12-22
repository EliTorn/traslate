import pymongo
from app import translate_to_hebrew

url = "mongodb+srv://eli:DxhkMWiiylHIq3eB@atlascluster.m6tavxq.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(url)

# Create a database
db: object = client["translate"]

# Create a collection
collection: object = db["translate"]


def connect(word: str) -> None:
    """
    the fanc get the name and picture and int of amount and insert this into the database
    """
    translate_word = translate_to_hebrew(word)
    d: object = {"word": word, 'translate': translate_word}

    collection.insert_one(d)


def show() -> object:
    """
    the func return the all date the in database
    \n
    -> return object :
    """

    data: object = collection.find()
    return data


def delete_word_from_mongo(condition):
    try:
        collection.delete_one({'word': f"{condition}"})

    except Exception as e:
        print(f"An error occurred: {e}")

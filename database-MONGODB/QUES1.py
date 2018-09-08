import pymongo
try:
    client = pymongo.MongoClient()
    database = client['yashasvi']
    collection = database['students']
finally :
    if database:
        print("Students database has been created!")
    if collection:
        print("students table has been created")

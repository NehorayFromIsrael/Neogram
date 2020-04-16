import pymongo

def Func(database_name,collection_name):

    """ connect to mongodb and return database and collection"""


    ## ---- connect to mongo & create or switch databse ---- ##
    mongo = pymongo.MongoClient("127.0.0.1",27017)
    database = mongo[database_name]

    ## ---- return collection ---- ##
    return database[collection_name]

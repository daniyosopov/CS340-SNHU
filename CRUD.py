from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    matched_cunt = 0
    updated_cunt = 0
    deleted_cunt = 0

    def __init__(self, user, passwrod):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:36437/AAC' % (user, passwrod))
        # where xxxx is your unique port number
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            check_insert = self.database.animals.insert(data)  # data should be dictionary
            if check_insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty.")


    def read(self, element):
        if element is not None:
            data = self.database.animals.find(element, {"_id":False})
            if data is not None:
                return data
            else:
                raise Exception("Unsuccessful read.")
        else:
            data = self.database.animals.find({"_id":False})
            if data is not None:
                return data
            else:
                raise Exception("Unsuccessful read.")


    def update(self, element, update, options):
        if element is None and update is None :
            raise Exception("Can't be updated without selecting the element.\n Needs to have the updated data.")
        elif element is None:
            raise Exception("Can't be updated without selecting the element.")
        elif update is None :
            raise Exception("Needs to have the updated data.")
        else:
            if options is 'Many' or 'many' or 'MANY':
                data = self.database.animals.update_many(element, {"$set": update})
                if data is not None:
                    matched_cunt = data.matched_count
                    updated_cunt = data.modified_count
                    return print("Result({Matched: ", matched_cunt,", Updated: ", updated_cunt, "})")
                else:
                    raise Exception("Unsuccessful update.")

            elif options is 'one' or 'ONE' or 'One':
                data = self.database.animals.update_one(element, {"$set": update})
                if data is not None:
                    matched_cunt = data.matched_count
                    updated_cunt = data.modified_count
                    return print("Result({Matched: ", matched_cunt,", Updated: ", updated_cunt, "})")
                else:
                    raise Exception("Unsuccessful update.")

            else:
                data = self.database.animals.update_one(element, {"$set": update})
                if data is not None:
                    matched_cunt = data.matched_count
                    updated_cunt = data.modified_count
                    return print("Result({Matched: ", matched_cunt, ", Updated: ", updated_cunt, "})")
                else:
                    raise Exception("Unsuccessful update.")


    def delete(self, element, options):
        if element is None:
            raise Exception("Can't be delete data without selecting the element.")
        else:
            if options is 'Many' or 'many' or 'MANY':
                matched_cunt = self.database.animals.find(element).count()
                data = self.database.animals.delete_many(element)
                deleted_cunt = data.deleted_count
                if deleted_cunt > 0:
                    return print("Result({Matched: ", matched_cunt, ", deleted: ", matched_cunt, "})")
                else:
                    raise Exception("Unsuccessful delete.")

            elif options is 'one' or 'ONE' or 'One':
                matched_cunt = self.database.animals.find(element).count()
                data = self.database.animals.delete_one(element)
                deleted_cunt = data.deleted_count
                if deleted_cunt is 1:
                    return print("Result({Matched: ", matched_cunt, ", deleted: ", deleted_cunt, "})")
                else:
                    raise Exception("Unsuccessful delete.")

            else:
                matched_cunt = self.database.animals.find(element).count()
                data = self.database.animals.delete_one(element)
                deleted_cunt = data.deleted_count
                if deleted_cunt is 1:
                    return print("Result({Matched: ", matched_cunt, ", deleted: ", deleted_cunt,"})")
                else:
                    raise Exception("Unsuccessful delete.")


from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

class UserService:
    def __init__(self):
        try:
            connection_string = os.getenv('MONGO_URI')
            self.client = MongoClient(connection_string)
            self.database = self.client['conversemosdb']
            print("Conexión exitosa a la base de datos")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
    
    def find(self, query):
        collection = self.database['users'] 
        return collection.find(query)

    def find_one(self, query):
        collection = self.database['users'] 
        return collection.find_one(query)

    def insert_one(self, data):
        collection = self.database['users']
        collection.insert_one(data)

    def update_one(self, query, data):
        collection = self.database['users'] 
        update_data = {"$set": data} 
        collection.update_one(query, update_data)

    def delete_one(self, query):
        collection = self.database['users']
        collection.delete_one(query)

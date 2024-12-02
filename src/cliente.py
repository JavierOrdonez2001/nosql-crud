from pymongo import MongoClient
from bson.objectid import ObjectId

class Cliente:
    def __init__(self, client:MongoClient, db):
        self._db = client[db]
        self.cliente = self._db['clientes']
        

    def read_cliente(self):
        clienteStotage = []
        for cliente in self.cliente.find():
            clienteStotage.append(cliente)
        return clienteStotage

    def read_cliente_by_id(self, _id):  
       result = self.cliente.find_one({"_id":_id})
       return result     
       
    def create_cliente(self, data):
       try:
           result = self.cliente.insert_one(data)
           return result.inserted_id
       except Exception as e:
           return f'algo salio mal: {e}'
       

    def delete_cliente(self, _id):
        try:
            result = self.cliente.delete_one({"_id":_id})
            return result.deleted_count
        except Exception as e:
            return f'algo salio mal: {e}'
        
        
    def update_cliente(self, _id, data):
        try:
            result = self.cliente.update_one({"_id": _id}, {"$set": data})
            return result.modified_count
        except Exception as e:
            return f'algo salio mal: {e}'
        

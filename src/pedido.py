from pymongo import MongoClient
from bson.objectid import ObjectId


class Pedido:
    def __init__(self, client:MongoClient, db):
        self._db = client[db]
        self._pedidos = self._db['pedidos']

    
    def read_pedidos(self):
        pedidoStorage = []    
        for pedido in self._pedidos.find():
            pedidoStorage.append(pedido)
        return pedidoStorage

    def read_pedidos_by_id(self, _id):       
        pedido = self._pedidos.find_one({"_id": ObjectId(_id)})
        return pedido

    def create_pedido(self, data):
        try:
            result = self._pedidos.insert_one(data)
            return result.inserted_id
        except Exception as e:
            return f'Algo a salido mal: {e}'

    def delete_pedido(self, _id):
        try:
            result = self._pedidos.delete_one({"_id": ObjectId(_id)})
            return result.deleted_count
        except Exception as e:
            return f'algo salio mal: {e}'
        
    def update_pedido(self, _id, data):
        try:
            result = self._pedidos.update_one({"_id": ObjectId(_id)}, {"$set": data})
            return result.modified_count
        except Exception as e:
            return f'algo salio mal: {e}'

  
        

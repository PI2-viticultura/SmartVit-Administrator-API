
from settings import load_database_params
import pymongo


class MongoDB():
    def __init__(self):
        self.params = load_database_params()
        try:
            self.client = pymongo.MongoClient(
                **self.params, serverSelectionTimeoutMS=10
            )

        except Exception as err:
            print(f'Erro ao conectar no banco de dados: {err}')

    def test_connection(self):
        try:
            self.client.server_info()
            return True
        except Exception as err:
            print(f'Erro ao conectar no banco de dados: {err}')
            return False

    def close_connection(self):
        self.client.close()

    def get_collection(self, collection):
        db = self.client['smart-dev']
        collection = db[collection]
        return collection

    def insert_one(self, body, collection):
        try:
            collection = self.get_collection(collection)
            return collection.insert_one(body)

        except Exception as err:
            print(f'Erro ao inserir no banco de dados: {err}')
            return False

    def update_one(self, body, collection):
        try:
            collection = self.get_collection(collection)
            collection.update_one(
                {"id": body["id"]},
                {"$set": {body}}
            )

        except Exception as err:
            print(f'Erro ao atualizar no banco de dados: {err}')

    def delete_one(self, identifier, collection):
        try:
            collection = self.get_collection(collection)
            res = collection.delete_one({"id": identifier})
            if res.deleted_count == 1:
                print(f'Objeto {identifier} removido com sucesso')
            else:
                print(f'Erro ao remover o objeto {identifier}:'
                      ' nenhum objeto com este id encontrado em' + collection)
        except Exception as err:
            print(f'Erro ao deletar no banco de dados: {err}')

    def get_one(self, identifier, collection):
        collection = self.get_collection(collection)
        document = collection.find_one({"_id": identifier})
        return document

from flask_restx import Model, fields

product_api_model = Model('product', {'uuid': fields.String, 'name': fields.String,})


class ProductModel:
    def __init__(self, uuid: str, name: str):
        self.uuid = uuid
        self.name = name

from flask import abort, request
from flask_restx import Resource
from project.ext.serializer import ProductSchema

from project.service.product_service import (delete_product, get_all_products,
                                             get_one_product, post_product,
                                             update_product)

product_schema_list = ProductSchema(many=True)
product_schema = ProductSchema(many=False)


class ProductResource(Resource):

    def get(self):
        products = get_all_products()
        return product_schema_list.dump(products), 200

    def post(self):
        try:
            product_data = request.json
            post_product(product_data)
            return {"message": "Produto cadastrado com sucesso!"}, 201
        
        except Exception as e:
            return {"error": str(e)}, 400


class ProductResourceID(Resource):

    def get(self, id):
        if product := get_one_product(id):
            return product_schema.dump(product), 200  # type: ignore
        else:
            return {"error": f"Produto com ID {id} não encontrado."}, 404
        
        
    def patch(self, id):
        try:
            product_data = request.json
            result = update_product(id, product_data)

            if "error" in result:
                abort(404, message=result["error"])
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500


    def delete(self, id):
        try:
            result = delete_product(id)

            if "error" in result:
                return {"error": result["error"]}, 404
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500
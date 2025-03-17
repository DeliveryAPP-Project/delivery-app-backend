import json

from flask import abort, request
from flask_restx import Resource

from project.doc_model.doc_models import api, doc_product_model
from project.ext.serializer import ProductSchema
from project.service.product_service import (
    delete_product,
    get_all_products,
    get_one_product,
    post_product,
    update_product,
)
from project.utils.redis_utils import (
    delete_redis_value,
    get_redis_value,
    set_redis_value,
)

product_schema_list = ProductSchema(many=True)
product_schema = ProductSchema(many=False)


class ProductResource(Resource):
    def get(self):
        try:
            has_gluten = request.args.get("has_gluten")
            has_lactose = request.args.get("has_lactose")
            is_vegan = request.args.get("is_vegan")
            is_vegetarian = request.args.get("is_vegetarian")
            key_redis = "products"
            products = get_redis_value(key_redis)
            if products:
                return products
            products = get_all_products(
                has_gluten, has_lactose, is_vegan, is_vegetarian
            )
            products = product_schema_list.dump(products)
            set_redis_value(key_redis, json.dumps(products))
            return products, 200
        except Exception as e:
            return {"error": str(e)}, 400

    @api.expect(doc_product_model)
    def post(self):
        try:
            product_data = request.json
            post_product(product_data)  # type: ignore
            delete_redis_value("products")
            return {"message": "Produto cadastrado com sucesso!"}, 201

        except Exception as e:
            return {"error": str(e)}, 400


class ProductResourceID(Resource):
    def get(self, id: int):
        try:
            if product := get_one_product(id):
                return product_schema.dump(product), 200  # type: ignore
            else:
                return {"error": f"Produto com ID {id} não encontrado."}, 404
        except Exception as e:
            return {"error": str(e)}, 400

    @api.expect(doc_product_model)
    def patch(self, id: int):
        try:
            product_data = request.json
            result = update_product(id, product_data)  # type: ignore

            if "error" in result:
                abort(404, message=result["error"])
            delete_redis_value("clients")
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500

    def delete(self, id: int):
        try:
            result = delete_product(id)

            if "error" in result:
                return {"error": result["error"]}, 404
            delete_redis_value("products")
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500

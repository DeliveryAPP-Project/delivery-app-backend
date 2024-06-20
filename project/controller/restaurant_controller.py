import json
from flask import request
from flask_restx import Resource
from project.ext.serializer import RestaurantSchema

from project.service.restaurant_service import (
    delete_restaurant,
    get_all_restaurants,
    get_one_restaurant,
    post_restaurant,
    update_restaurant,
)
from project.utils.redis_utils import (
    delete_redis_value,
    get_redis_value,
    set_redis_value,
)

restaurant_schema_list = RestaurantSchema(many=True)
restaurant_schema = RestaurantSchema(many=False)


class RestaurantResource(Resource):
    def get(self):
        key_redis = "restaurants"
        restaurants = get_redis_value(key_redis)
        if restaurants:
            return restaurants
        restaurants = get_all_restaurants()
        restaurants = restaurant_schema_list.dump(restaurants)
        set_redis_value(key_redis, json.dumps(restaurants))
        return restaurants, 200

    def post(self):
        try:
            restaurant_data = request.json
            post_restaurant(restaurant_data)
            delete_redis_value("restaurants")
            return {"message": "Restaurante cadastrado com sucesso!"}, 201

        except Exception as e:
            return {"error": str(e)}, 400


class RestaurantResourceID(Resource):
    def get(self, id):
        print("a")
        if restaurant := get_one_restaurant(id):
            return restaurant  # type: ignore
        else:
            return {"error": f"Restaurante com ID {id} não encontrado."}, 404

    def patch(self, id):
        try:
            restaurant_data = request.json
            result = update_restaurant(id, restaurant_data)

            if "error" in result:
                return {"error": result["error"]}, 404
            delete_redis_value("clients")
            return {"message": result["message"]}, 200

        except Exception as e:
            # print(e)
            return {"error": str(e)}, 500

    def delete(self, id):
        try:
            result = delete_restaurant(id)

            if "error" in result:
                return {"error": result["error"]}, 404
            delete_redis_value("restaurants")
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500

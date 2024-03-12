from flask import abort, request
from flask_restx import Resource
from project.ext.serializer import RestaurantSchema

from project.service.restaurant_service import (delete_restaurant,
                                                get_all_restaurants,
                                                get_one_restaurant,
                                                post_restaurant,
                                                update_restaurant)

restaurant_schema_list = RestaurantSchema(many=True)
restaurant_schema = RestaurantSchema(many=False)


class RestaurantResource(Resource):

    def get(self):
        restaurants = get_all_restaurants()
        return restaurant_schema_list.dump(restaurants), 200


    def post(self):
        try:
            restaurant_data = request.json
            post_restaurant(restaurant_data)
            return {"message": "Restaurante cadastrado com sucesso!"}, 201
        
        except Exception as e:
            return {"error": str(e)}, 400


class RestaurantResourceID(Resource):

    def get(self, id):
        if restaurant := get_one_restaurant(id):
            return restaurant_schema.dump(restaurant), 200  # type: ignore
        else:
            return {"error": f"Restaurante com ID {id} não encontrado."}, 404
        
        
    def patch(self, id):
        try:
            restaurant_data = request.json
            result = update_restaurant(id, restaurant_data)

            if "error" in result:
                abort(404, message=result["error"])
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500


    def delete(self, id):
        try:
            result = delete_restaurant(id)

            if "error" in result:
                return {"error": result["error"]}, 404
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500
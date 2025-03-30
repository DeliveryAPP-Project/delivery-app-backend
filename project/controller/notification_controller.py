from click import echo
from flask import request
from flask_restx import Resource


class NotificationResource(Resource):
    def post(self):
        try:
            notification_data = request.json
            if not isinstance(notification_data, dict):
                return {"error": "Invalid input"}, 400

            echo(notification_data)

            return {}, 200

        except Exception as e:
            return {"error": str(e)}, 400

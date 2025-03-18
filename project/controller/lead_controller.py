import re

from flask import request
from flask_restx import Resource

from project.doc_model.doc_models import api, lead_model
from project.service.lead_service import (
    post_lead,
)
from project.utils.redis_utils import (
    delete_redis_value,
)


class LeadResource(Resource):
    @api.expect(lead_model)
    def post(self):
        try:
            lead_data = request.json
            if not isinstance(lead_data, dict) or "email" not in lead_data:
                return {"error": "Invalid input, 'email' key is required"}, 400

            email = lead_data.get("email")

            valid = re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)  # type: ignore

            if not isinstance(email, str) or not valid:
                return {"error": "Invalid email format"}, 400

            post_lead(lead_data)  # type: ignore
            delete_redis_value("leads")
            return {"message": "Lead cadastrado com sucesso!"}, 201

        except Exception as e:
            return {"error": str(e)}, 400

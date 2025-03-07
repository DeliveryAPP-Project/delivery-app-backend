from project.models.lead_model import Lead

from ..ext.database import db


def post_lead(data_lead: dict):
    lead = Lead(**data_lead)
    try:
        db.session.add(lead)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

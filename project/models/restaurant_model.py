from ..ext.database import db


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    classification = db.Column(db.Float(precision=3), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    url_image_logo = db.Column(db.String(), nullable=True)
    url_image_banner = db.Column(db.String(), nullable=True)
    products = db.relationship(
        "Product", backref="restaurant", lazy=True
    )

    def __init__(
        self,
        name,
        description,
        classification,
        location,
        url_image_logo,
        url_image_banner,
    ):
        self.name = name
        self.description = description
        self.classification = classification
        self.location = location
        self.url_image_logo = url_image_logo
        self.url_image_banner = url_image_banner

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "classification": self.classification,
            "location": self.location,
            "url_image_logo": self.url_image_logo,
            "url_image_banner": self.url_image_banner,
        }

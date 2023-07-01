from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class OrderModel(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer())
    customer_ref = db.Column(db.String(80))
    quantity = db.Column(db.Integer())

    def __init__(self, product_id, customer_ref, quantity):
        self.product_id = product_id
        self.customer_ref = customer_ref
        self.quantity = quantity

    def __repr__(self):
        return f"{self.id}:{self.customer_ref}"

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

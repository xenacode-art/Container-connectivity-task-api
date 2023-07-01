from flask import Flask, render_template, request, redirect
from models import db, OrderModel
import os
import json
import functools

print = functools.partial(print, flush=True)


app = Flask(__name__)

DB_HOST = os.environ["DB_HOST"]
DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
DB_NAME = os.environ["DB_NAME"]
API_PORT = os.environ["API_PORT"]

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route("/order/create", methods=["POST"])
def create():
    if request.method == "POST":
        product_id = request.form["product_id"]
        customer_ref = request.form["customer_ref"]
        quantity = request.form["quantity"]
        order = OrderModel(
            product_id=product_id, customer_ref=customer_ref, quantity=quantity
        )
        db.session.add(order)
        db.session.commit()
        return order.as_dict()


@app.route("/order")
def RetrieveList():
    return [o.as_dict() for o in OrderModel.query.all()]


@app.route("/order/<int:id>")
def RetrieveOrder(id):
    order = OrderModel.query.filter_by(id=id).first()
    if order:
        return order.as_dict()
    return {"error": f"Order {id} does not exist"}


app.run(host="0.0.0.0", port=API_PORT)

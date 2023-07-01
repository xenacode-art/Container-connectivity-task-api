from time import sleep
from requests import get
import random
import requests
import os
import string
import functools

print = functools.partial(print, flush=True)


API_HOST = os.environ["API_HOST"]
API_PORT = os.environ["API_PORT"]

print(API_HOST)

while True:
    sleep_time = random.randint(1, 30)
    print(f"Sleeping for {sleep_time}")
    sleep(sleep_time)

    path = random.choice(["", "create", "id"])

    if path == "":
        response = requests.get(f"http://{API_HOST}:{API_PORT}/order")
        print(response)

    if path == "create":
        payload = {
            "product_id": random.randint(1, 20),
            "customer_ref": "".join(
                random.choices(string.ascii_uppercase + string.digits, k=15)
            ),
            "quantity": random.randint(1, 5),
        }

        response = requests.post(
            f"http://{API_HOST}:{API_PORT}/order/create", data=payload
        )
        print(response)

    if path == "id":
        order_id = random.randint(1, 50)
        response = requests.get(f"http://{API_HOST}:{API_PORT}/order/{order_id}")
        print(response)

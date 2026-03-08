import requests
from configuration import URL_SERVICE, CREATE_ORDERS_ENDPOINT, GET_ORDERS_TRACK_ENDPOINT

def create_order(order_data):
    url = f"{URL_SERVICE}{CREATE_ORDERS_ENDPOINT}"
    response = requests.post(url, json=order_data)
    return response

def get_order_by_track(track):
    url = f"{URL_SERVICE}{GET_ORDERS_TRACK_ENDPOINT}"
    response = requests.get(url, params={"t": track})
    return response
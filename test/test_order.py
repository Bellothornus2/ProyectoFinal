import pytest
import json
from app import app
from services.order import get_order_last_id

@pytest.mark.get_order_all
def test_get_order_all():
	client_api = app.test_client()
	response = client_api.get("/order")
	assert b"data" in response.data

@pytest.mark.get_order_by_id
def test_get_order():
	client_api = app.test_client()
	order_file = open("./utilities/order.json")
	order_data = json.load(order_file)
	order_created = client_api.post("/order",json=order_data["create"])
	order_created_id = json.loads(order_created.data)["data"]["id"]
	response = client_api.get("/order/%s" % (order_created_id))
	assert order_created_id == json.loads(response.data)["data"]["id"]

@pytest.mark.create_order ##invocar con pytest -m create_order
def test_add_order():
	client_api = app.test_client()
	order_file = open("./utilities/order.json")
	order_data = json.load(order_file)
	result = client_api.post("/order",json=order_data["create"])
	last_id = get_order_last_id()
	last_order = client_api.get("order/%s" % (last_id))
	assert result.data == last_order.data
	#client_api.delete("/order/%s" % (last_id))

@pytest.mark.order_last_id ##invocar con pytest -m order_last_id
def test_order_last_id():
	client_api = app.test_client()
	last_id = get_order_last_id()
	last_order = client_api.get("order/%s" % (last_id))
	last_order_id = json.loads(last_order.data)["data"]["id"]
	assert last_order_id == last_id

@pytest.mark.put_order
def test_put_order():
	client_api = app.test_client()
	order_file = open("./utilities/order.json")
	order_data = json.load(order_file)
	post_response = client_api.post("/order",json=order_data["create"])
	order_post_id = json.loads(post_response.data)["data"]["id"]
	put_response = client_api.put("/order/%s" % (order_post_id), json=order_data["update"])
	order_updated = client_api.get("/order/%s" % (order_post_id))
	assert put_response.data == order_updated.data
	#test.delete("/order", json={"name": "hola que ase", "sell_in": 80, "quality": 80})

@pytest.mark.delete_order
def test_delete_order():
	client_api = app.test_client()
	order_file = open("./utilities/order.json")
	order_data = json.load(order_file)
	post_result = client_api.post("/order",json=order_data["create"])
	last_id = get_order_last_id()
	delete_result = client_api.delete("/order/%s" % (last_id))
	assert post_result.data == delete_result.data

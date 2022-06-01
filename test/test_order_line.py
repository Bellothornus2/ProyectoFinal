import pytest
import json
from app import app
from services.order_line import get_order_line_last_id

@pytest.mark.get_order_line_all
def test_get_order_line_all():
	client_api = app.test_client()
	response = client_api.get("/order_line")
	assert b"data" in response.data

@pytest.mark.get_order_line_by_id
def test_get_order_line():
	client_api = app.test_client()
	order_line_file = open("./utilities/order_line.json")
	order_line_data = json.load(order_line_file)
	order_line_created = client_api.post("/order_line",json=order_line_data["create"])
	order_line_created_id = json.loads(order_line_created.data)["data"]["id"]
	response = client_api.get("/order_line/%s" % (order_line_created_id))
	assert order_line_created_id == json.loads(response.data)["data"]["id"]

@pytest.mark.create_order_line ##invocar con pytest -m create_order_line
def test_add_order_line():
	client_api = app.test_client()
	order_line_file = open("./utilities/order_line.json")
	order_line_data = json.load(order_line_file)
	result = client_api.post("/order_line",json=order_line_data["create"])
	last_id = get_order_line_last_id()
	last_order_line = client_api.get("order_line/%s" % (last_id))
	assert result.data == last_order_line.data
	#client_api.delete("/order_line/%s" % (last_id))

@pytest.mark.order_line_last_id ##invocar con pytest -m order_line_last_id
def test_order_line_last_id():
	client_api = app.test_client()
	last_id = get_order_line_last_id()
	last_order_line = client_api.get("order_line/%s" % (last_id))
	last_order_line_id = json.loads(last_order_line.data)["data"]["id"]
	assert last_order_line_id == last_id

@pytest.mark.put_order_line
def test_put_order_line():
	client_api = app.test_client()
	order_line_file = open("./utilities/order_line.json")
	order_line_data = json.load(order_line_file)
	post_response = client_api.post("/order_line",json=order_line_data["create"])
	order_line_post_id = json.loads(post_response.data)["data"]["id"]
	put_response = client_api.put("/order_line/%s" % (order_line_post_id), json=order_line_data["update"])
	order_line_updated = client_api.get("/order_line/%s" % (order_line_post_id))
	assert put_response.data == order_line_updated.data
	#test.delete("/order_line", json={"name": "hola que ase", "sell_in": 80, "quality": 80})

@pytest.mark.delete_order_line
def test_delete_order_line():
	client_api = app.test_client()
	order_line_file = open("./utilities/order_line.json")
	order_line_data = json.load(order_line_file)
	post_result = client_api.post("/order_line",json=order_line_data["create"])
	last_id = get_order_line_last_id()
	delete_result = client_api.delete("/order_line/%s" % (last_id))
	assert post_result.data == delete_result.data

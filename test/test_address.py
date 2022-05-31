import pytest
import json
from app import app
from services.address import get_address_last_id

@pytest.mark.get_address_all
def test_get_address_all():
	client_api = app.test_client()
	response = client_api.get("/address")
	assert b"data" in response.data

@pytest.mark.get_address_by_id
def test_get_address():
	client_api = app.test_client()
	address_file = open("./utilities/address.json")
	address_data = json.load(address_file)
	address_created = client_api.post("/address",json=address_data["create"])
	address_created_id = json.loads(address_created.data)["data"]["id"]
	response = client_api.get("/address/%s" % (address_created_id))
	assert address_created_id == json.loads(response.data)["data"]["id"]

@pytest.mark.create_address ##invocar con pytest -m create_address
def test_add_address():
	client_api = app.test_client()
	address_file = open("./utilities/address.json")
	address_data = json.load(address_file)
	result = client_api.post("/address",json=address_data["create"])
	last_id = get_address_last_id()
	last_address = client_api.get("address/%s" % (last_id))
	assert result.data == last_address.data
	#client_api.delete("/address/%s" % (last_id))

@pytest.mark.address_last_id ##invocar con pytest -m address_last_id
def test_address_last_id():
	client_api = app.test_client()
	last_id = get_address_last_id()
	last_address = client_api.get("address/%s" % (last_id))
	last_address_id = json.loads(last_address.data)["data"]["id"]
	assert last_address_id == last_id

@pytest.mark.put_address
def test_put_address():
	client_api = app.test_client()
	address_file = open("./utilities/address.json")
	address_data = json.load(address_file)
	post_response = client_api.post("/address",json=address_data["create"])
	address_post_id = json.loads(post_response.data)["data"]["id"]
	put_response = client_api.put("/address/%s" % (address_post_id), json=address_data["update"])
	address_updated = client_api.get("/address/%s" % (address_post_id))
	assert put_response.data == address_updated.data
	#test.delete("/address", json={"name": "hola que ase", "sell_in": 80, "quality": 80})

@pytest.mark.delete_address
def test_delete_address():
	client_api = app.test_client()
	address_file = open("./utilities/address.json")
	address_data = json.load(address_file)
	post_result = client_api.post("/address",json=address_data["create"])
	last_id = get_address_last_id()
	delete_result = client_api.delete("/address/%s" % (last_id))
	assert post_result.data == delete_result.data

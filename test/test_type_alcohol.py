import pytest
import json
from app import app
from services.type_alcohol import get_type_alcohol_last_id

@pytest.mark.get_type_alcohol_all
def test_get_type_alcohol_all():
	client_api = app.test_client()
	response = client_api.get("/type_alcohol")
	assert b"data" in response.data

@pytest.mark.get_type_alcohol_by_id
def test_get_type_alcohol():
	client_api = app.test_client()
	type_alcohol_file = open("./utilities/type_alcohol.json")
	type_alcohol_data = json.load(type_alcohol_file)
	type_alcohol_created = client_api.post("/type_alcohol",json=type_alcohol_data["create"])
	type_alcohol_created_id = json.loads(type_alcohol_created.data)["data"]["id"]
	response = client_api.get("/type_alcohol/%s" % (type_alcohol_created_id))
	assert type_alcohol_created_id == json.loads(response.data)["data"]["id"]

@pytest.mark.create_type_alcohol ##invocar con pytest -m create_type_alcohol
def test_add_type_alcohol():
	client_api = app.test_client()
	type_alcohol_file = open("./utilities/type_alcohol.json")
	type_alcohol_data = json.load(type_alcohol_file)
	result = client_api.post("/type_alcohol",json=type_alcohol_data["create"])
	last_id = get_type_alcohol_last_id()
	last_type_alcohol = client_api.get("type_alcohol/%s" % (last_id))
	assert result.data == last_type_alcohol.data
	#client_api.delete("/type_alcohol/%s" % (last_id))

@pytest.mark.type_alcohol_last_id ##invocar con pytest -m type_alcohol_last_id
def test_type_alcohol_last_id():
	client_api = app.test_client()
	last_id = get_type_alcohol_last_id()
	last_type_alcohol = client_api.get("type_alcohol/%s" % (last_id))
	last_type_alcohol_id = json.loads(last_type_alcohol.data)["data"]["id"]
	assert last_type_alcohol_id == last_id

@pytest.mark.put_type_alcohol
def test_put_type_alcohol():
	client_api = app.test_client()
	type_alcohol_file = open("./utilities/type_alcohol.json")
	type_alcohol_data = json.load(type_alcohol_file)
	post_response = client_api.post("/type_alcohol",json=type_alcohol_data["create"])
	type_alcohol_post_id = json.loads(post_response.data)["data"]["id"]
	put_response = client_api.put("/type_alcohol/%s" % (type_alcohol_post_id), json=type_alcohol_data["update"])
	type_alcohol_updated = client_api.get("/type_alcohol/%s" % (type_alcohol_post_id))
	assert put_response.data == type_alcohol_updated.data
	#test.delete("/type_alcohol", json={"name": "hola que ase", "sell_in": 80, "quality": 80})

@pytest.mark.delete_type_alcohol
def test_delete_type_alcohol():
	client_api = app.test_client()
	type_alcohol_file = open("./utilities/type_alcohol.json")
	type_alcohol_data = json.load(type_alcohol_file)
	post_result = client_api.post("/type_alcohol",json=type_alcohol_data["create"])
	last_id = get_type_alcohol_last_id()
	delete_result = client_api.delete("/type_alcohol/%s" % (last_id))
	assert post_result.data == delete_result.data

import pytest
import json
from app import app
from services.subtype_alcohol import get_subtype_alcohol_last_id

@pytest.mark.get_subtype_alcohol_all
def test_get_subtype_alcohol_all():
	client_api = app.test_client()
	response = client_api.get("/subtype_alcohol")
	assert b"data" in response.data

@pytest.mark.get_subtype_alcohol_by_id
def test_get_subtype_alcohol():
	client_api = app.test_client()
	subtype_alcohol_file = open("./utilities/subtype_alcohol.json")
	subtype_alcohol_data = json.load(subtype_alcohol_file)
	subtype_alcohol_created = client_api.post("/subtype_alcohol",json=subtype_alcohol_data["create"])
	subtype_alcohol_created_id = json.loads(subtype_alcohol_created.data)["data"]["id"]
	response = client_api.get("/subtype_alcohol/%s" % (subtype_alcohol_created_id))
	assert subtype_alcohol_created_id == json.loads(response.data)["data"]["id"]

@pytest.mark.create_subtype_alcohol ##invocar con pytest -m create_subtype_alcohol
def test_add_subtype_alcohol():
	client_api = app.test_client()
	subtype_alcohol_file = open("./utilities/subtype_alcohol.json")
	subtype_alcohol_data = json.load(subtype_alcohol_file)
	result = client_api.post("/subtype_alcohol",json=subtype_alcohol_data["create"])
	last_id = get_subtype_alcohol_last_id()
	last_subtype_alcohol = client_api.get("subtype_alcohol/%s" % (last_id))
	assert result.data == last_subtype_alcohol.data
	#client_api.delete("/subtype_alcohol/%s" % (last_id))

@pytest.mark.subtype_alcohol_last_id ##invocar con pytest -m subtype_alcohol_last_id
def test_subtype_alcohol_last_id():
	client_api = app.test_client()
	last_id = get_subtype_alcohol_last_id()
	last_subtype_alcohol = client_api.get("subtype_alcohol/%s" % (last_id))
	last_subtype_alcohol_id = json.loads(last_subtype_alcohol.data)["data"]["id"]
	assert last_subtype_alcohol_id == last_id

@pytest.mark.put_subtype_alcohol
def test_put_subtype_alcohol():
	client_api = app.test_client()
	subtype_alcohol_file = open("./utilities/subtype_alcohol.json")
	subtype_alcohol_data = json.load(subtype_alcohol_file)
	post_response = client_api.post("/subtype_alcohol",json=subtype_alcohol_data["create"])
	subtype_alcohol_post_id = json.loads(post_response.data)["data"]["id"]
	put_response = client_api.put("/subtype_alcohol/%s" % (subtype_alcohol_post_id), json=subtype_alcohol_data["update"])
	subtype_alcohol_updated = client_api.get("/subtype_alcohol/%s" % (subtype_alcohol_post_id))
	assert put_response.data == subtype_alcohol_updated.data
	#test.delete("/subtype_alcohol", json={"name": "hola que ase", "sell_in": 80, "quality": 80})

@pytest.mark.delete_subtype_alcohol
def test_delete_subtype_alcohol():
	client_api = app.test_client()
	subtype_alcohol_file = open("./utilities/subtype_alcohol.json")
	subtype_alcohol_data = json.load(subtype_alcohol_file)
	post_result = client_api.post("/subtype_alcohol",json=subtype_alcohol_data["create"])
	last_id = get_subtype_alcohol_last_id()
	delete_result = client_api.delete("/subtype_alcohol/%s" % (last_id))
	assert post_result.data == delete_result.data

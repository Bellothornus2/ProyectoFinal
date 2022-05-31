import pytest
import json
from app import app
from services.ingredient_alcohol import get_ingredient_alcohol_last_id

@pytest.mark.get_ingredient_alcohol_all
def test_get_ingredient_alcohol_all():
	client_api = app.test_client()
	response = client_api.get("/ingredient_alcohol")
	assert b"data" in response.data

@pytest.mark.get_ingredient_alcohol_by_id
def test_get_ingredient_alcohol():
	client_api = app.test_client()
	ingredient_alcohol_file = open("./utilities/ingredient_alcohol.json")
	ingredient_alcohol_data = json.load(ingredient_alcohol_file)
	ingredient_alcohol_created = client_api.post("/ingredient_alcohol",json=ingredient_alcohol_data["create"])
	ingredient_alcohol_created_id = json.loads(ingredient_alcohol_created.data)["data"]["id"]
	response = client_api.get("/ingredient_alcohol/%s" % (ingredient_alcohol_created_id))
	assert ingredient_alcohol_created_id == json.loads(response.data)["data"]["id"]

@pytest.mark.create_ingredient_alcohol ##invocar con pytest -m create_ingredient_alcohol
def test_add_ingredient_alcohol():
	client_api = app.test_client()
	ingredient_alcohol_file = open("./utilities/ingredient_alcohol.json")
	ingredient_alcohol_data = json.load(ingredient_alcohol_file)
	result = client_api.post("/ingredient_alcohol",json=ingredient_alcohol_data["create"])
	last_id = get_ingredient_alcohol_last_id()
	last_ingredient_alcohol = client_api.get("ingredient_alcohol/%s" % (last_id))
	assert result.data == last_ingredient_alcohol.data
	#client_api.delete("/ingredient_alcohol/%s" % (last_id))

@pytest.mark.ingredient_alcohol_last_id ##invocar con pytest -m ingredient_alcohol_last_id
def test_ingredient_alcohol_last_id():
	client_api = app.test_client()
	last_id = get_ingredient_alcohol_last_id()
	last_ingredient_alcohol = client_api.get("ingredient_alcohol/%s" % (last_id))
	last_ingredient_alcohol_id = json.loads(last_ingredient_alcohol.data)["data"]["id"]
	assert last_ingredient_alcohol_id == last_id

@pytest.mark.put_ingredient_alcohol
def test_put_ingredient_alcohol():
	client_api = app.test_client()
	ingredient_alcohol_file = open("./utilities/ingredient_alcohol.json")
	ingredient_alcohol_data = json.load(ingredient_alcohol_file)
	post_response = client_api.post("/ingredient_alcohol",json=ingredient_alcohol_data["create"])
	ingredient_alcohol_post_id = json.loads(post_response.data)["data"]["id"]
	put_response = client_api.put("/ingredient_alcohol/%s" % (ingredient_alcohol_post_id), json=ingredient_alcohol_data["update"])
	ingredient_alcohol_updated = client_api.get("/ingredient_alcohol/%s" % (ingredient_alcohol_post_id))
	assert put_response.data == ingredient_alcohol_updated.data
	#test.delete("/ingredient_alcohol", json={"name": "hola que ase", "sell_in": 80, "quality": 80})

@pytest.mark.delete_ingredient_alcohol
def test_delete_ingredient_alcohol():
	client_api = app.test_client()
	ingredient_alcohol_file = open("./utilities/ingredient_alcohol.json")
	ingredient_alcohol_data = json.load(ingredient_alcohol_file)
	post_result = client_api.post("/ingredient_alcohol",json=ingredient_alcohol_data["create"])
	last_id = get_ingredient_alcohol_last_id()
	delete_result = client_api.delete("/ingredient_alcohol/%s" % (last_id))
	assert post_result.data == delete_result.data

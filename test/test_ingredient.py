import pytest
import json
from app import app
from services.ingredient import get_ingredient_last_id

@pytest.mark.get_ingredient_all
def test_get_ingredient_all():
	client_api = app.test_client()
	response = client_api.get("/ingredient")
	assert b"data" in response.data

@pytest.mark.get_ingredient_by_id
def test_get_ingredient():
	client_api = app.test_client()
	ingredient_file = open("./utilities/ingredient.json")
	ingredient_data = json.load(ingredient_file)
	ingredient_created = client_api.post("/ingredient",json=ingredient_data["create"])
	ingredient_created_id = json.loads(ingredient_created.data)["data"]["id"]
	response = client_api.get("/ingredient/%s" % (ingredient_created_id))
	assert ingredient_created_id == json.loads(response.data)["data"]["id"]

@pytest.mark.create_ingredient ##invocar con pytest -m create_ingredient
def test_add_ingredient():
	client_api = app.test_client()
	ingredient_file = open("./utilities/ingredient.json")
	ingredient_data = json.load(ingredient_file)
	result = client_api.post("/ingredient",json=ingredient_data["create"])
	last_id = get_ingredient_last_id()
	last_ingredient = client_api.get("ingredient/%s" % (last_id))
	assert result.data == last_ingredient.data
	#client_api.delete("/ingredient/%s" % (last_id))

@pytest.mark.ingredient_last_id ##invocar con pytest -m ingredient_last_id
def test_ingredient_last_id():
	client_api = app.test_client()
	last_id = get_ingredient_last_id()
	last_ingredient = client_api.get("ingredient/%s" % (last_id))
	last_ingredient_id = json.loads(last_ingredient.data)["data"]["id"]
	assert last_ingredient_id == last_id

@pytest.mark.put_ingredient
def test_put_ingredient():
	client_api = app.test_client()
	ingredient_file = open("./utilities/ingredient.json")
	ingredient_data = json.load(ingredient_file)
	post_response = client_api.post("/ingredient",json=ingredient_data["create"])
	ingredient_post_id = json.loads(post_response.data)["data"]["id"]
	put_response = client_api.put("/ingredient/%s" % (ingredient_post_id), json=ingredient_data["update"])
	ingredient_updated = client_api.get("/ingredient/%s" % (ingredient_post_id))
	assert put_response.data == ingredient_updated.data
	#test.delete("/ingredient", json={"name": "hola que ase", "sell_in": 80, "quality": 80})

@pytest.mark.delete_ingredient
def test_delete_ingredient():
	client_api = app.test_client()
	ingredient_file = open("./utilities/ingredient.json")
	ingredient_data = json.load(ingredient_file)
	post_result = client_api.post("/ingredient",json=ingredient_data["create"])
	last_id = get_ingredient_last_id()
	delete_result = client_api.delete("/ingredient/%s" % (last_id))
	assert post_result.data == delete_result.data

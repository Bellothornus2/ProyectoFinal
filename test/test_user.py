import pytest
import json
from app import app
from services.user import get_user_last_id

@pytest.mark.get_user_all
def test_get_user_all():
	client_api = app.test_client()
	response = client_api.get("/user")
	assert b"data" in response.data

@pytest.mark.get_user_by_id
def test_get_user():
	client_api = app.test_client()
	user_file = open("./utilities/user.json")
	user_data = json.load(user_file)
	user_created = client_api.post("/user",json=user_data["create"])
	user_created_id = json.loads(user_created.data)["data"]["id"]
	response = client_api.get("/user/%s" % (user_created_id))
	assert user_created_id == json.loads(response.data)["data"]["id"]

@pytest.mark.create_user ##invocar con pytest -m create_user
def test_add_user():
	client_api = app.test_client()
	user_file = open("./utilities/user.json")
	user_data = json.load(user_file)
	result = client_api.post("/user",json=user_data["create"])
	last_id = get_user_last_id()
	last_user = client_api.get("user/%s" % (last_id))
	assert result.data == last_user.data
	#client_api.delete("/user/%s" % (last_id))

@pytest.mark.user_last_id ##invocar con pytest -m user_last_id
def test_user_last_id():
	client_api = app.test_client()
	last_id = get_user_last_id()
	last_user = client_api.get("user/%s" % (last_id))
	last_user_id = json.loads(last_user.data)["data"]["id"]
	assert last_user_id == last_id

@pytest.mark.put_user
def test_put_user():
	client_api = app.test_client()
	user_file = open("./utilities/user.json")
	user_data = json.load(user_file)
	post_response = client_api.post("/user",json=user_data["create"])
	user_post_id = json.loads(post_response.data)["data"]["id"]
	put_response = client_api.put("/user/%s" % (user_post_id), json=user_data["update"])
	user_updated = client_api.get("/user/%s" % (user_post_id))
	assert put_response.data == user_updated.data
	#test.delete("/user", json={"name": "hola que ase", "sell_in": 80, "quality": 80})

@pytest.mark.delete_user
def test_delete_user():
	client_api = app.test_client()
	user_file = open("./utilities/user.json")
	user_data = json.load(user_file)
	post_result = client_api.post("/user",json=user_data["create"])
	last_id = get_user_last_id()
	delete_result = client_api.delete("/user/%s" % (last_id))
	assert post_result.data == delete_result.data

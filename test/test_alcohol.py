import pytest
import json
from app import app
from services.alcohol import get_alcohol_last_id

@pytest.mark.get_alcohol_all
def test_get_alcohol_all():
	client_api = app.test_client()
	response = client_api.get("/alcohol")
	assert b"data" in response.data

@pytest.mark.get_alcohol_by_id
def test_get_alcohol():
	client_api = app.test_client()
	alcohol_file = open("./utilities/alcohol.json")
	alcohol_data = json.load(alcohol_file)
	alcohol_created = client_api.post("/alcohol",json=alcohol_data["create"])
	alcohol_created_id = json.loads(alcohol_created.data)["data"]["id"]
	response = client_api.get("/alcohol/%s" % (alcohol_created_id))
	assert alcohol_created_id == json.loads(response.data)["data"]["id"]

@pytest.mark.create_alcohol ##invocar con pytest -m create_alcohol
def test_add_alcohol():
	client_api = app.test_client()
	alcohol_file = open("./utilities/alcohol.json")
	alcohol_data = json.load(alcohol_file)
	result = client_api.post("/alcohol",json=alcohol_data["create"])
	last_id = get_alcohol_last_id()
	last_alcohol = client_api.get("alcohol/%s" % (last_id))
	assert result.data == last_alcohol.data
	#client_api.delete("/alcohol/%s" % (last_id))

@pytest.mark.alcohol_last_id ##invocar con pytest -m alcohol_last_id
def test_alcohol_last_id():
	client_api = app.test_client()
	last_id = get_alcohol_last_id()
	last_alcohol = client_api.get("alcohol/%s" % (last_id))
	last_alcohol_id = json.loads(last_alcohol.data)["data"]["id"]
	assert last_alcohol_id == last_id

@pytest.mark.delete_alcohol
def test_delete_alcohol():
	client_api = app.test_client()
	alcohol_file = open("./utilities/alcohol.json")
	alcohol_data = json.load(alcohol_file)
	post_result = client_api.post("/alcohol",json=alcohol_data["create"])
	last_id = get_alcohol_last_id()
	delete_result = client_api.delete("/alcohol/%s" % (last_id))
	assert post_result.data == delete_result.data

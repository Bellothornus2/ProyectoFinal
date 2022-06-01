import pytest
import json
from app import app
from services.credit_card import get_credit_card_last_id

@pytest.mark.get_credit_card_all
def test_get_credit_card_all():
	client_api = app.test_client()
	response = client_api.get("/credit_card")
	assert b"data" in response.data

@pytest.mark.get_credit_card_by_id
def test_get_credit_card():
	client_api = app.test_client()
	credit_card_file = open("./utilities/credit_card.json")
	credit_card_data = json.load(credit_card_file)
	credit_card_created = client_api.post("/credit_card",json=credit_card_data["create"])
	credit_card_created_id = json.loads(credit_card_created.data)["data"]["id"]
	response = client_api.get("/credit_card/%s" % (credit_card_created_id))
	assert credit_card_created_id == json.loads(response.data)["data"]["id"]

@pytest.mark.create_credit_card ##invocar con pytest -m create_credit_card
def test_add_credit_card():
	client_api = app.test_client()
	credit_card_file = open("./utilities/credit_card.json")
	credit_card_data = json.load(credit_card_file)
	result = client_api.post("/credit_card",json=credit_card_data["create"])
	last_id = get_credit_card_last_id()
	last_credit_card = client_api.get("credit_card/%s" % (last_id))
	assert result.data == last_credit_card.data
	#client_api.delete("/credit_card/%s" % (last_id))

@pytest.mark.credit_card_last_id ##invocar con pytest -m credit_card_last_id
def test_credit_card_last_id():
	client_api = app.test_client()
	last_id = get_credit_card_last_id()
	last_credit_card = client_api.get("credit_card/%s" % (last_id))
	last_credit_card_id = json.loads(last_credit_card.data)["data"]["id"]
	assert last_credit_card_id == last_id

@pytest.mark.put_credit_card
def test_put_credit_card():
	client_api = app.test_client()
	credit_card_file = open("./utilities/credit_card.json")
	credit_card_data = json.load(credit_card_file)
	post_response = client_api.post("/credit_card",json=credit_card_data["create"])
	credit_card_post_id = json.loads(post_response.data)["data"]["id"]
	put_response = client_api.put("/credit_card/%s" % (credit_card_post_id), json=credit_card_data["update"])
	credit_card_updated = client_api.get("/credit_card/%s" % (credit_card_post_id))
	assert put_response.data == credit_card_updated.data
	#test.delete("/credit_card", json={"name": "hola que ase", "sell_in": 80, "quality": 80})

@pytest.mark.delete_credit_card
def test_delete_credit_card():
	client_api = app.test_client()
	credit_card_file = open("./utilities/credit_card.json")
	credit_card_data = json.load(credit_card_file)
	post_result = client_api.post("/credit_card",json=credit_card_data["create"])
	last_id = get_credit_card_last_id()
	delete_result = client_api.delete("/credit_card/%s" % (last_id))
	assert post_result.data == delete_result.data

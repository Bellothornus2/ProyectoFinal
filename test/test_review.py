import pytest
import json
from app import app
from services.review import get_review_last_id

@pytest.mark.get_review_all
def test_get_review_all():
	client_api = app.test_client()
	response = client_api.get("/review")
	assert b"data" in response.data

@pytest.mark.get_review_by_id
def test_get_review():
	client_api = app.test_client()
	review_file = open("./utilities/review.json")
	review_data = json.load(review_file)
	review_created = client_api.post("/review",json=review_data["create"])
	review_created_id = json.loads(review_created.data)["data"]["id"]
	response = client_api.get("/review/%s" % (review_created_id))
	assert review_created_id == json.loads(response.data)["data"]["id"]

@pytest.mark.create_review ##invocar con pytest -m create_review
def test_add_review():
	client_api = app.test_client()
	review_file = open("./utilities/review.json")
	review_data = json.load(review_file)
	result = client_api.post("/review",json=review_data["create"])
	last_id = get_review_last_id()
	last_review = client_api.get("review/%s" % (last_id))
	assert result.data == last_review.data
	#client_api.delete("/review/%s" % (last_id))

@pytest.mark.review_last_id ##invocar con pytest -m review_last_id
def test_review_last_id():
	client_api = app.test_client()
	last_id = get_review_last_id()
	last_review = client_api.get("review/%s" % (last_id))
	last_review_id = json.loads(last_review.data)["data"]["id"]
	assert last_review_id == last_id

@pytest.mark.put_review
def test_put_review():
	client_api = app.test_client()
	review_file = open("./utilities/review.json")
	review_data = json.load(review_file)
	post_response = client_api.post("/review",json=review_data["create"])
	review_post_id = json.loads(post_response.data)["data"]["id"]
	put_response = client_api.put("/review/%s" % (review_post_id), json=review_data["update"])
	review_updated = client_api.get("/review/%s" % (review_post_id))
	assert put_response.data == review_updated.data
	#test.delete("/review", json={"name": "hola que ase", "sell_in": 80, "quality": 80})

@pytest.mark.delete_review
def test_delete_review():
	client_api = app.test_client()
	review_file = open("./utilities/review.json")
	review_data = json.load(review_file)
	post_result = client_api.post("/review",json=review_data["create"])
	last_id = get_review_last_id()
	delete_result = client_api.delete("/review/%s" % (last_id))
	assert post_result.data == delete_result.data

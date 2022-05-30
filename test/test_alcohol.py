import pytest
import json
from app import app
from services.alcohol import get_alcohol_last_id

@pytest.mark.create_alcohol ##invocar con pytest - create_alcohol
def test_add_alcohol():
	client_api = app.test_client()
	result = client_api.post("/alcohol",json={
    "name":"Cerveza Generica 2",
    "alcohol_grade": 2.5,
    "price": 1.80,
    "brand": "Cosas",
    "type_alcohol_id":1,
    "subtype_alcohol_id":1,
    "description":"Prueba de Creacio de Cerveza Pale Ale"
	})
	last_id = get_alcohol_last_id()
	last_alcohol = client_api.get("alcohol/%s" % (last_id))
	assert result.data == last_alcohol.data
	client_api.delete("/alcohol/%s" % (last_id))

@pytest.mark.alcohol_last_id ##invocar con pytest - alcohol_last_id
def test_alcohol_last_id():
	client_api = app.test_client()
	last_id = get_alcohol_last_id()
	last_alcohol = client_api.get("alcohol/%s" % (last_id))
	last_alcohol_id = json.loads(last_alcohol.data)["data"]["id"]
	assert last_alcohol_id == last_id

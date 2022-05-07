import pytest
from app import app


@pytest.mark.get_item
def test_get_aged_brie():
    test = app.test_client()
    data = test.get("/")
    items = data.get_json()
    for item in items.items():
        item_id = item[0]
        break
    item_to_retrieve = "/item/%s" % item_id
    response = test.get(item_to_retrieve)
    assert b'{"name":' in response.data


@pytest.mark.get_item_fail
def test_get_aged_brie_fail():
    test = app.test_client()
    response = test.get("/item/0")
    assert b'{"none":"null"' in response.data

import pytest
from app import app


@pytest.mark.put_item
def test_put_item():
    test = app.test_client()
    test.post("/item", json={"name": "hola", "sell_in": 2, "quality": 3})
    get_all_items = test.get("/")
    dict_items = get_all_items.get_json()
    for item in dict_items.items():
        if item["name"] == "hola":
            test.put(
                "/item",
                json={
                    "id": item[0],
                    "new_name": "hola que ase",
                    "new_sell_in": 80,
                    "new_quality": 80,
                },
            )
    get_all_items = test.get("/")
    assert b'{"name":"hola que ase","quality":80,"sell_in":80}' in get_all_items.data
    test.delete("/item", json={"name": "hola que ase", "sell_in": 80, "quality": 80})

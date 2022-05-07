from . import base
import pytest
from controller import hello_world

base.api.add_resource(hello_world.HelloWorld, "/")


@pytest.fixture
def root():
    response = base.app.test_client().get("/")
    return response

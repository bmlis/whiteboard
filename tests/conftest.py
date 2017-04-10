import pytest
from whiteboard.app import create_app
from whiteboard.app import ApplicationContext


@pytest.fixture
def test_app():
    app = create_app(ApplicationContext())
    return app.test_client()

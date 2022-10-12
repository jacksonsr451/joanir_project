import pytest

from src.framework.app import create_app


@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['DEBUG'] = False
    return app

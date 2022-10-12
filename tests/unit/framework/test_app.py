def test_app_is_created(app):
    print(app.name)
    assert app.name == 'src.framework.app'


def test_if_config_is_loaded(config):
    assert config['DEBUG'] is False
    assert config['TESTING'] is True


def test_request_return_404(client):
    assert client.get('/url').status_code == 404

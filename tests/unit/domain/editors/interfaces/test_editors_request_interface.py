import pytest

from src.domain.editors.interfaces.editors_request import EditorsRequestInterface


@pytest.fixture(scope='module')
def editors_request_interface():
    return EditorsRequestInterface


def test_should_be_has_methods(editors_request_interface):
    assert getattr(editors_request_interface, 'get_id')
    assert getattr(editors_request_interface, 'get_username')
    assert getattr(editors_request_interface, 'get_email')
    assert getattr(editors_request_interface, 'get_password')
    assert getattr(editors_request_interface, 'is_admin')
    assert getattr(editors_request_interface, 'get_created_at')
    assert getattr(editors_request_interface, 'get_updated_at')

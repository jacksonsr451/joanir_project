import pytest

from src.domain.editors.interfaces.editors_repository_interface import EditorsRepositoryInterface


@pytest.fixture(scope='module')
def editors_repository_interface():
    return EditorsRepositoryInterface


def test_should_be_has_methods(editors_repository_interface):
    assert getattr(editors_repository_interface, 'show')
    assert getattr(editors_repository_interface, 'view')
    assert getattr(editors_repository_interface, 'create')
    assert getattr(editors_repository_interface, 'update')
    assert getattr(editors_repository_interface, 'delete')

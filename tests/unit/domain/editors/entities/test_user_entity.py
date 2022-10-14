import uuid

import pytest

from src.domain.editors.entities.user_entity import UserEntity
from tests.adapters.requests.editors_request_test import EditorsRequestTest


@pytest.fixture(scope='module')
def user_entity():
    return UserEntity(
        request=EditorsRequestTest(
            id=str(uuid.uuid4()),
            username='Username Test',
            email='email@email.com',
            password='123456789',
            admin=True,
            created_at='14/10/2022',
            updated_at='14/10/2022'
        )
    )


def test_should_be_has_methods(user_entity):
    assert hasattr(user_entity, 'get_id')
    assert hasattr(user_entity, 'get_username')
    assert hasattr(user_entity, 'get_email')
    assert hasattr(user_entity, 'get_password')
    assert hasattr(user_entity, 'is_admin')
    assert hasattr(user_entity, 'get_created_at')
    assert hasattr(user_entity, 'get_updated_at')


def test_should_be_return_types(user_entity):
    assert type(user_entity.get_id()) == str
    assert type(user_entity.get_username()) == str
    assert type(user_entity.get_email()) == str
    assert type(user_entity.get_password()) == str
    assert type(user_entity.is_admin()) == bool
    assert type(user_entity.get_created_at()) == str
    assert type(user_entity.get_updated_at()) == str

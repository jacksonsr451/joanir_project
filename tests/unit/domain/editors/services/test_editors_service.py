import uuid

import pytest

from src.domain.editors.entities.user_entity import UserEntity
from src.domain.editors.interfaces.editors_repository_interface import EditorsRepositoryInterface
from src.domain.editors.services.editors_services import EditorsServices
from tests.adapters.requests.editors_request_test import EditorsRequestTest


@pytest.fixture(scope='module')
def editors_services(user_entity):
    return EditorsServices(TestEditorsRepository(user_entity))


def test_should_be_has_methods(editors_services):
    assert getattr(editors_services, 'show')
    assert getattr(editors_services, 'view')
    assert getattr(editors_services, 'create')
    assert getattr(editors_services, 'update')
    assert getattr(editors_services, 'delete')


def test_should_be_return_types(editors_services, user_entity):
    assert type(editors_services.show()) == list
    assert type(editors_services.view(user_entity.get_id())) == UserEntity
    assert editors_services.create(user_entity) is None
    assert editors_services.update(user_entity) is None
    assert editors_services.delete(user_entity.get_id()) is None


class TestEditorsRepository(EditorsRepositoryInterface):
    def __init__(self, user_entity):
        self.__list = list()
        self.__list.append(user_entity)
        self.user = user_entity

    def show(self) -> list:
        return self.__list

    def view(self, id: str) -> UserEntity:
        return self.user

    def create(self, user: UserEntity) -> None:
        pass

    def update(self, user: UserEntity) -> None:
        pass

    def delete(self, id: str) -> None:
        pass


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
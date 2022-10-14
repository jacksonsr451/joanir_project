from src.domain.editors.entities.user_entity import UserEntity
from src.domain.editors.interfaces.editors_repository_interface import EditorsRepositoryInterface


class EditorsServices:
    def __init__(self, repository: EditorsRepositoryInterface):
        self.__repository = repository

    def show(self) -> list:
        return self.__repository.show()

    def view(self, id: str) -> UserEntity:
        return self.__repository.view(id=id)

    def create(self, user: UserEntity) -> None:
        self.__repository.create(user=user)

    def update(self, user: UserEntity) -> None:
        self.__repository.update(user=user)

    def delete(self, id: str) -> None:
        self.__repository.delete(id=id)

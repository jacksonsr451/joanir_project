from abc import ABC

from src.domain.editors.entities.user_entity import UserEntity


class EditorsRepositoryInterface(ABC):
    def show(self) -> list:
        """This method is required!"""

    def view(self, id: str) -> UserEntity:
        """This method is required!"""

    def create(self, user: UserEntity) -> None:
        """This method is required!"""

    def update(self, user: UserEntity) -> None:
        """This method is required!"""

    def delete(self, id: str) -> None:
        """This method is required!"""

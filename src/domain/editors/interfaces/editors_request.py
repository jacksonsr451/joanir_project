from abc import ABC, abstractmethod


class EditorsRequestInterface(ABC):
    @abstractmethod
    def get_id(self) -> str:
        """This method is required"""

    @abstractmethod
    def get_username(self) -> str:
        """This method is required"""

    @abstractmethod
    def get_email(self) -> str:
        """This method is required"""

    @abstractmethod
    def get_password(self) -> str:
        """This method is required"""

    @abstractmethod
    def is_admin(self) -> bool:
        """This method is required"""

    @abstractmethod
    def get_created_at(self) -> str:
        """This method is required"""

    @abstractmethod
    def get_updated_at(self) -> str:
        """This method is required"""

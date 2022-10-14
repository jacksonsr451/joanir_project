from datetime import datetime

from src.domain.editors.interfaces.editors_request import (
    EditorsRequestInterface,
)


class UserEntity:
    __id: str
    __username: str
    __email: str
    __password: str
    __admin: bool = False
    __created_at: str = datetime.now().strftime('dd%/MM%/YY%')
    __updated_at: str = datetime.now().strftime('dd%/MM%/YY%')

    def __init__(self, request: EditorsRequestInterface):
        self.__id = request.get_id()
        self.__username = request.get_username()
        self.__email = request.get_email()
        self.__password = request.get_password()
        self.__admin = request.is_admin()
        self.__created_at = request.get_created_at()
        self.__updated_at = request.get_updated_at()

    def get_id(self) -> str:
        return self.__id

    def get_username(self) -> str:
        return self.__username

    def get_email(self) -> str:
        return self.__email

    def get_password(self) -> str:
        return self.__password

    def is_admin(self) -> bool:
        return self.__admin

    def get_created_at(self) -> str:
        return self.__created_at

    def get_updated_at(self) -> str:
        return self.__updated_at

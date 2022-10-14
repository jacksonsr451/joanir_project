from src.domain.editors.interfaces.editors_request import (
    EditorsRequestInterface,
)


class EditorsRequestTest(EditorsRequestInterface):
    id: str
    username: str
    email: str
    password: str
    admin: bool
    created_at: str
    updated_at: str

    def __init__(
        self,
        id: str = None,
        username: str = None,
        email: str = None,
        password: str = None,
        admin: bool = None,
        created_at: str = None,
        updated_at: str = None,
    ):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.admin = admin
        self.created_at = created_at
        self.updated_at = updated_at

    def get_id(self) -> str:
        return self.id

    def get_username(self) -> str:
        return self.username

    def get_email(self) -> str:
        return self.email

    def get_password(self) -> str:
        return self.password

    def is_admin(self) -> bool:
        return self.admin

    def get_created_at(self) -> str:
        return self.created_at

    def get_updated_at(self) -> str:
        return self.updated_at

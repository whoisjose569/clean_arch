#pylint: disable= use-implicit-booleaness-not-comparison
from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_finder import UserFinder


def test_find():
    first_name = 'meunome'
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)

    assert repo.select_user_attributes["first_name"] == first_name

    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []

def test_find_error_in_valid_name():

    first_name = 'meunome'
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
    except Exception as expection:
        assert str(expection) == "Nome invalido para a busca"

def test_find_error_on_long_name():

    first_name = 'meunomesadasweqeqwdsadsaewqewqdsaasd'
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
    except Exception as expection:
        assert str(expection) == "Nome muito grande para busca"

def test_find_error_user_not_found():
    class UsersRepositoryError(UsersRepositorySpy):
        def select_user(self, first_name: str):
            return []

    first_name = 'meunome'
    repo = UsersRepositoryError()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
    except Exception as expection:
        assert str(expection) == 'Usuario nao encontrado'

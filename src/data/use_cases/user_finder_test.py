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

def test_find_error_in_vlaid_name():

    first_name = 'meunome123'
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        response = user_finder.find(first_name)
    except Exception as expection:
        assert str(expection) == "Nome invalido para a busca"

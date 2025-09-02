import pytest
import allure
from pages.user_page import UserPage

user_page = UserPage()

@allure.feature("CRUD Operations")
def test_crud_operations():
    with allure.step("Create table"):
        user_page.create_table()

    with allure.step("Insert user"):
        user_page.insert_user("Alice")
        users = user_page.select_users()
        assert any(u[1] == "Alice" for u in users)

    with allure.step("Update user"):
        user_id = users[0][0]
        user_page.update_user(user_id, "Charlie")
        users = user_page.select_users()
        assert any(u[1] == "Charlie" for u in users)

    with allure.step("Delete user"):
        user_page.delete_user(user_id)
        users = user_page.select_users()
        assert all(u[0] != user_id for u in users)

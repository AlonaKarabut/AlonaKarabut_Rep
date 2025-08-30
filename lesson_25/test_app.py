from app import create_table, insert_user, update_user, delete_user, select_users


def test_crud_operations():
    create_table()

    insert_user("Bob")
    users = select_users()
    assert any(u[1] == "Bob" for u in users)

    user_id = users[0][0]
    update_user(user_id, "Charlie")
    users = select_users()
    assert any(u[1] == "Charlie" for u in users)

    delete_user(user_id)
    users = select_users()
    assert all(u[0] != user_id for u in users)

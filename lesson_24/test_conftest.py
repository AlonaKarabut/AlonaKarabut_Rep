import time

def test_user_registration(open_registration_modal, fill_registration_form, submit_registration, driver):
    email = f"test{int(time.time())}@mail.com"
    fill_registration_form("Alona", "Test", email, "Qwerty1234")
    submit_registration()
    assert "panel" in driver.current_url, "Registration failed"

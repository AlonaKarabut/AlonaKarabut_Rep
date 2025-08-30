import pytest
from selenium import webdriver
from homework_23_AlonaKarabut import TrackingPage

@pytest.fixture
def driver():
    print("Open Chrome")
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    print("Close Chrome")
    driver.quit()

@pytest.mark.parametrize("tracking_number, expected_status", [
    ("20400472401797", "Отримана"),  # це реальний ттн моєї посилки)
])
def test_tracking_status(driver, tracking_number, expected_status):
    print(f"\n=== Start of the test: {tracking_number} ===")
    page = TrackingPage(driver)
    page.open()
    page.enter_tracking_number(tracking_number)
    status = page.get_status()
    assert expected_status in status, f"ER: {expected_status}, AR: {status}"

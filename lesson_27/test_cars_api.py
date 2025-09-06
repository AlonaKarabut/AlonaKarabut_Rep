import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

# ===============================
# Логування
# ===============================
logger = logging.getLogger("cars_api_test")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('test_search.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# ===============================
# Константи
# ===============================
BASE_URL = "http://127.0.0.1:8080"


# ===============================
# Фікстура авторизації
# ===============================
@pytest.fixture(scope='class')
def auth_session():
    """Фікстура для авторизації та повернення сесії з токеном"""
    session = requests.Session()
    auth = HTTPBasicAuth('test_user', 'test_pass')

    # Додаємо "/" до кінця, щоб уникнути 404
    response = session.post(f"{BASE_URL}/auth", auth=auth)

    if response.status_code != 200:
        logger.error(f"Auth failed: {response.status_code} - {response.text}")
        raise Exception("Не вдалося авторизуватися. Перевірте сервер і URL /auth/")

    access_token = response.json()['access_token']
    session.headers.update({'Authorization': f'Bearer {access_token}'})
    logger.info("Authenticated successfully")
    return session


# ===============================
# Клас тестів
# ===============================
@pytest.mark.usefixtures("auth_session")
class TestCarsAPI:

    # Параметризовані набори даних для sort_by і limit
    @pytest.mark.parametrize("sort_by,limit", [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 7),
        ("brand", 10),
        ("price", 1),
        ("year", 8),
        ("engine_volume", 0)  # limit=0 означає "без обмеження"
    ])
    def test_search_cars(self, auth_session, sort_by, limit):
        url = f"{BASE_URL}/cars?sort_by={sort_by}&limit={limit}"
        response = auth_session.get(url)

        logger.info(f"Request URL: {url}")
        logger.info(f"Response status: {response.status_code}")
        logger.info(f"Response body: {response.text}")

        # Перевірка статусу
        assert response.status_code == 200, f"GET /cars failed: {response.text}"

        data = response.json()

        # Перевірка обмеження
        if limit > 0:
            assert len(data) <= limit, f"Returned {len(data)} cars, expected <= {limit}"
        else:
            # limit=0 означає "без обмеження", перевіряємо просто, що повертається список
            assert isinstance(data, list), "Expected a list of cars"
import requests
import logging
from requests.auth import HTTPBasicAuth
import json

# ----------- Логування -----------
class FlushFileHandler(logging.FileHandler):
    def emit(self, record):
        super().emit(record)
        self.flush()

logger = logging.getLogger("cars_test_logger")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
file_handler = FlushFileHandler("test_search.log", mode="w", encoding="utf-8")

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.handlers.clear()
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.propagate = False

# ----------- Конфігурація -----------
BASE_URL = "http://127.0.0.1:8080"
USERNAME = "test_user"
PASSWORD = "test_pass"

# ----------- Набори параметрів для GET /cars -----------
test_data = [
    {"sort_by": "price", "limit": 5},
    {"sort_by": "price", "limit": 10},
    {"sort_by": "year", "limit": 5},
    {"sort_by": "year", "limit": 10},
    {"sort_by": "engine_volume", "limit": 3},
    {"sort_by": "brand", "limit": 7},
    {"sort_by": "price", "limit": 1},
]

# ----------- Функція аутентифікації -----------
def auth_session():
    logger.info("Пробуємо аутентифікацію...")
    session = requests.Session()
    try:
        resp = session.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth(USERNAME, PASSWORD))
        resp.raise_for_status()
        access_token = resp.json().get("access_token")
        if not access_token:
            raise Exception("Токен доступу не отримано")
        session.headers.update({"Authorization": "Bearer " + access_token})
        logger.info("Аутентифікація пройшла, токен отримано")
        return session
    except requests.exceptions.RequestException as e:
        logger.error(f"Аутентифікація не пройшла: {e}")
        raise

# ----------- Основна функція для запуску -----------

def main():
    session = auth_session()
    for params in test_data:
        try:
            logger.info(f"Тестуємо /cars із sort_by={params['sort_by']}, limit={params['limit']}")
            resp = session.get(f"{BASE_URL}/cars", params=params)
            resp.raise_for_status()
            cars = resp.json()

            # Форматуємо результат для друку
            formatted_result = json.dumps(cars, indent=4, ensure_ascii=False)

            # Лог і друк у консоль
            logger.info(f"Результат: {formatted_result}")
            print(f"\nРезультат для sort_by={params['sort_by']}, limit={params['limit']}:\n{formatted_result}")

        except requests.exceptions.RequestException as e:
            logger.error(f"Помилка GET /cars: {e}")
            print(f"Помилка GET /cars для параметрів {params}: {e}")

if __name__ == "__main__":
    main()

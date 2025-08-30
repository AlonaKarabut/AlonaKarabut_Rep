from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TrackingPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tracking.novaposhta.ua/#/uk"

    def open(self):
        print(f"Opening the page: {self.url}")
        self.driver.get(self.url)

        WebDriverWait(self.driver, 30).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        for _ in range(5):
            try:
                input_elem = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter TTN']"))
                )
                if input_elem.is_displayed():
                    break
            except:
                time.sleep(5)

    def enter_tracking_number(self, tracking_number):
        print(f"Вводимо номер ТТН: {tracking_number}")
        input_elem = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "en"))
        )
        input_elem.clear()
        input_elem.send_keys(tracking_number)

        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "np-number-input-desktop-btn-search-en"))
        )
        button.click()

    def get_status(self):
        try:
            status_elem = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".header__status-text"))
            )
            status_text = status_elem.text
            print(f"Status: {status_text}")
            return status_text
        except Exception as e:
            print(f"Didn`t get status: {e}")
            return None
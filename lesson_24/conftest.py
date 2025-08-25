import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def sign_up_btn(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Sign up']")


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def first_name_input(self):
        return self.driver.find_element(By.NAME, "name")

    @property
    def last_name_input(self):
        return self.driver.find_element(By.NAME, "lastName")

    @property
    def email_input(self):
        return self.driver.find_element(By.NAME, "email")

    @property
    def password_input(self):
        return self.driver.find_element(By.NAME, "password")

    @property
    def repeat_password_input(self):
        return self.driver.find_element(By.NAME, "repeatPassword")

    @property
    def register_btn(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Register']")


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    yield driver
    driver.quit()


@pytest.fixture
def home_page(driver):
    return HomePage(driver)


@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)


@pytest.fixture
def open_registration_modal(driver, home_page):
    home_page.sign_up_btn.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.NAME, "name")))
    return True


@pytest.fixture
def fill_registration_form(registration_page):
    def _fill(name, last_name, email, password):
        registration_page.first_name_input.send_keys(name)
        registration_page.last_name_input.send_keys(last_name)
        registration_page.email_input.send_keys(email)
        registration_page.password_input.send_keys(password)
        registration_page.repeat_password_input.send_keys(password)
    return _fill


@pytest.fixture
def submit_registration(registration_page, driver):
    def _submit():
        registration_page.register_btn.click()
        WebDriverWait(driver, 5).until(EC.url_contains("panel"))
    return _submit

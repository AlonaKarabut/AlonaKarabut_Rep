from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8000/dz.html")
    driver.maximize_window()

    driver.switch_to.frame("frame1")
    driver.find_element(By.ID, "input1").send_keys("Frame1_Secret")
    driver.find_element(By.TAG_NAME, "button").click()

    alert = Alert(driver)
    alert_text = alert.text
    alert.accept()

    driver.switch_to.default_content()

    driver.switch_to.frame("frame2")
    driver.find_element(By.ID, "input2").send_keys("Frame2_Secret")
    driver.find_element(By.TAG_NAME, "button").click()

    alert = Alert(driver)
    alert_text = alert.text
    alert.accept()

    driver.switch_to.default_content()

finally:
    time.sleep(1)
    driver.quit()

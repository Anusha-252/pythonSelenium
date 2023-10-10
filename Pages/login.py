import time

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from basetest import setup1, teardown


@pytest.fixture(scope="module")
def driver():
    driver = setup1()
    yield driver
    teardown(driver)

@pytest.mark.parametrize("phoneNumber, password, expected_error", [
    ("", "", "You can't leave this empty."),  # Empty phone number and password
    ("9814078236", "", "You can't leave this empty."),  # Empty password
    ("", "anushhasa", "You can't leave this empty."),  # Empty phone number
    ("9874373788", "ashdsdj", "Incorrect username or password"),  # Invalid credentials
    ("9814078236", "dashainaayo456", "")])
def login(phoneNumber, password, expected_error, driver):
    login_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='bld-txt']"))
    )
    login_link.click()

    # Find the input fields for phone number/email and password
    phoneNumber_input = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
    )
    password_input = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
    )

    # Enter the login credentials
    phoneNumber_input.send_keys(phoneNumber)
    password_input.send_keys(password)

    # Find and click the login button
    login_button = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'LOGIN')]"))
    )
    login_button.click()

    #Check for the presence of error message
    if expected_error:
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{expected_error}')]"))
        )
        print("assert error_message.text == expected_error")

    time.sleep(10)
    driver.quit()




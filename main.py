import pytest
from selenium import webdriver
from login import test_login
from category import category

if __name__ == "__main__":
    pytest.main(["-v","basetest.py"])
    driver = webdriver.Chrome()
    logged_in = test_login(phoneNumber,password,driver)

    if logged_in:
        category(driver)
    pytest.main(["-v", "login.py"])
    pytest.main(["-v", "category.py"])
    # pytest.main(["-v", "add_to_cart_test.py"])
    # pytest.main(["-v", "checkout_test.py"])

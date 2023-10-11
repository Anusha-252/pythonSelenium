from selenium import webdriver


def setup1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.daraz.com.np/#")
    return driver

def setup2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://member.daraz.com.np/user/profile#/")
    return driver


def teardown(driver):
    driver.quit()
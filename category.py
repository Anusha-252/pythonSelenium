import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from basetest import setup2, teardown


@pytest.fixture(scope="module")
def driver():
    driver = setup2()
    yield driver
    teardown(driver)


def category(driver):
    categoryLocate = driver.find_element(By.XPATH, "//span[@class='lzd-site-menu-nav-category-text']")
    womens_fashion = driver.find_element(By.XPATH, "//span[text()='Women's Fashion']")
    traditional_clothing=driver.find_element(By.XPATH, "//span[contains(text(), 'Traditional Clothing')]")
    saree=driver.find_element(By.XPATH,"//span[text()='Saree']")

    # Create an ActionChains object
    action_chains = ActionChains(driver)
    action_chains.move_to_element(categoryLocate).move_to_element(womens_fashion).move_to_element(traditional_clothing).move_to_element(saree).click().perform()
    driver.quit()

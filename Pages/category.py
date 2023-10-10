import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BasePage import BasePage
from basetest import BaseTest
from config import TestData


class Categories(BasePage):

    # @pytest.fixture(scope="module")
    # def driver():
    #     driver = setup2()
    #     yield driver
    #     teardown(driver)
    def __init__(self, driver):
        super().__int__(driver)
        self.driver.get(TestData.BASE_URL)
        self.wait=WebDriverWait(self.driver,30)



    def category(self):

        # categoryLocate = self.driver.find_element(By.XPATH, "//span[@class='lzd-site-menu-nav-category-text']")
        # womens_fashion = self.driver.find_element(By.XPATH, r'//span[text()="Women's Beauty"]')
        health_beauty=self.driver.find_element(By.XPATH,'//span[text()="Health & Beauty"]')
        beauty_tools = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Beauty Tools')]")
        # saree = self.driver.find_element(By.XPATH, "//span[text()='Saree']")

        # Create an ActionChains object
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(health_beauty).move_to_element(
            beauty_tools).click().perform()

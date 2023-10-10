import time

import pytest

from BasePage import BasePage
from Pages.category import Categories
from basetest import BaseTest
from config import TestData



class Test_Category(BaseTest):


    def test_cat(self):
        self.cat= Categories(self.driver)
        self.cat.category()


from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        self.should_be_empty_product_list()
        self.should_be_empty_basket_message()

    def should_be_empty_product_list(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY_ITEM_LIST), \
            "There are no items should be in basket"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "There is no empty basket message"

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_promo_url()
        self.should_be_add_to_basket_button()
        self.should_add_product_to_basket()
        self.should_be_order_confirmation()

    def should_be_promo_url(self):
        assert "newYear" in self.browser.current_url, "There is no promo"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket btn is not presented"

    def should_add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        time.sleep(4)

    def should_be_order_confirmation(self):
        element = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(
            ProductPageLocators.ORDER_CONFIRM))     # Распаковка кортежа происходит внутри самой функции (* - не нужно)
        assert element, "Order confirmation is not presented"



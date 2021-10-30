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
        self.should_be_product_confirmation()
        self.should_be_price_confirmation()

    def should_be_promo_url(self):
        assert "promo" in self.browser.current_url, "There is no promo"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket btn is not presented"

    def should_add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        # time.sleep(300)

    def should_be_product_confirmation(self):
        title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)

        message = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(
            ProductPageLocators.PRODUCT_CONFIRM_MESSAGE))   # Распаковка кортежа происходит внутри метода (* - не нужна)

        assert message.text == title.text, f"Product confirmation is not correct. Should be: {title.text}"

    def should_be_price_confirmation(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)

        message = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(
            ProductPageLocators.PRICE_CONFIRM_MESSAGE))   # Распаковка кортежа происходит внутри метода (* - не нужна)

        assert message.text == price.text, f"Price confirmation is not correct. Should be: {price.text}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_CONFIRM_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_CONFIRM_MESSAGE), \
            "Success message is not disappear"

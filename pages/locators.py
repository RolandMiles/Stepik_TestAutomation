from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn:nth-child(1)")


class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_EMPTY_ITEM_LIST = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".content h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".content .price_color")
    PRODUCT_CONFIRM_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong")
    PRICE_CONFIRM_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner strong")

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .locators import BasePageLocators
import math


class BasePage():

    # Передача объектов браузера и URL, а также времени неявного ожидания
    # Transfer browser, url and implicitly waiting timeout
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Проверка на исчезновение элемента в течение заданного времени
    # Check for element disappear in waiting time
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # Проверка существования элемента на странице / Обработка исключения
    # Check is element presented on page
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Проверка на не появление элемента в течение заданного времени
    # Check for element not presented in waiting time
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).\
                until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # Переход на страницу логина
    # Go to login page
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    # Переход на страницу корзины
    # Go to basket page
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    # Открыть страницу по ссылке в браузере
    # Open page
    def open(self):
        self.browser.get(self.url)

    # Проверка наличия ссылки на логин
    # Check is login link presented
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # Решение квиза для получения проверочного кода
    # Solve quiz for checkung code
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

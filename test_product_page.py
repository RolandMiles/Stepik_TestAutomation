import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo_num',
                         [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason='bugged')), *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, promo_num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_num}"
    page = ProductPage(browser, link)       # инициализируем Page Object
    page.open()                             # открываем страницу
    page.add_product_to_basket()            # выполняем метод страницы


@pytest.mark.xfail(reason="Success message is presented")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)       # инициализируем Page Object
    page.open()                             # открываем страницу
    page.should_add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)       # инициализируем Page Object
    page.open()                             # открываем страницу
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Success message is not disappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)       # инициализируем Page Object
    page.open()                             # открываем страницу
    page.should_add_product_to_basket()
    page.should_disappear_success_message()
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Define test call parameters
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    # Get test option from parameters
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    # Testing in chrome
    if browser_name == "chrome":
        print("\n---Start browser chrome for test...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    # Testing in firefox
    elif browser_name == "firefox":
        print("\n---Start browser firefox for test...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)

    # Browser is not implemented
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\n---Quit browser...")
    browser.quit()

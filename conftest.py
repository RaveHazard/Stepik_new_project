import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language == "ru":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        browser.implicitly_wait(5)
    elif language == "en":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    elif language == "es":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    else:
        raise pytest.UsageError("=======you need choose language========")

    yield browser
    browser.quit()
    print("\n=========QUIT BROWSER=======")

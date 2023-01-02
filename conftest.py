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
        print('\n You choose fr language, start test....')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        browser.implicitly_wait(5)
    elif language == "en":
        print("You choose ru language, start test....")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    elif language == "es":
        print("You choose es language, start test....")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    else:
        raise pytest.UsageError("=======you need choose lang en, ru========")

    yield browser
    browser.quit()
    print("\n=========QUIT BROWSER=======")

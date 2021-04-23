import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: preferred language")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help = "Choose browser: firefox or chrome" )

@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart chrome browser for test..")

    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == 'chrome':
        browser = webdriver.Chrome(options=options)
    if browser_name =='firefox' :
        browser = webdriver.Firefox( options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Specify language param, e.g., --language=fr'
    )

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print(f"\nStart chrome browser for test with language: {user_language}...")

    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10) # Неявное ожидание для надежности
    yield browser
    print("\nQuit browser..")
    browser.quit()
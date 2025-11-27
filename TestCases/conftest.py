from selenium import webdriver
import pytest
def pytest_addoption(parser):
    parser.addoption("--browser", action="store",default="firefox",help="Type of browser: chrome, firefox, edge")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        print("Launching Chrome Browser.")
        driver = webdriver.Chrome()
    
    elif browser == 'firefox':
        print("Launching Firefox Browser.")
        driver = webdriver.Firefox()
    
    elif browser == 'edge':
        print("Launching Firefox Browser.")
        driver = webdriver.Edge()
    
    else:
        print("Invalid Browser, Launching Firefox browser.")
        driver = webdriver.Firefox()

    driver.maximize_window()
    yield driver
    driver.quit()
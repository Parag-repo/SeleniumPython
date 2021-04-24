from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="D:\\Programming\\Python\\drivers\\chromedriver.exe")
    # driver.maximize_window()
    return driver


# - Generating HTML reports
# pytest -v -s --html=Reports\report.html testCases/test_login.py
def pytest_configure(config):
    config.metadata['Project Name'] = 'nop Commerce'
    config.metadata['Module Name'] = 'Customer'
    config.metadata['Tester'] = 'XYZ'


@pytest.mark.filterwarnings
def pytest_metadata(metatdata):
    metatdata.pop("JAVA_HOME", None)
    metatdata.pop("Plugins", None)

# pytest -s -v testCases/test_login.py  ---- for normal execution
# pytest -s -v -n=2 testCases/test_login.py  ---- for parallel execution of 2 instances
# Below part is for reference, but not working at the moment
# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome(executable_path="D:\\Programming\\Python\\drivers\\chromedriver.exe")
#         print("Launching Chrome browser")
#     elif browser == 'edge':
#         driver = webdriver.Chrome(executable_path="D:\\Programming\\Python\\drivers\\msedgedriver.exe")
#         print("Launching Edge browser")
#     else:
#         driver = webdriver.Chrome(executable_path="D:\\Programming\\Python\\drivers\\chromedriver.exe")
#     driver.maximize_window()
#     return driver
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")

import pytest
from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="type1", help="my option: chrome or firefox or IE")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
       driver = webdriver.Chrome(executable_path="/Users/durga/PycharmProjects/pythonlearning/chromedriver.exe")
    elif browser_name == "firefox":
       driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "IE":
        print("Internet Explorer")

    # driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

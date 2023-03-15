import pytest
from selenium import webdriver
import time

# @pytest.fixture()
# def setup():
#     driver=webdriver.Chrome()
#     return driver

@pytest.fixture()
def setup(browser):

    if browser == 'internetexplorer':
        driver=webdriver.Ie()


    elif browser == 'firefox':
        driver=webdriver.Firefox()

    else:
        options = webdriver.ChromeOptions()  # Drive is closing auomatically to stop that used this
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser") #This will get the value from CLI/hooks

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")  #This will return browser value to setup method


#**********Pytest HTML Report**********
#It is hook for adding environment info to html reports

def pytest_configure(config):
    config._metadata['Project Name']='nop customers'
    config._metadata['Module Name'] ='Customers'
    config._metadata['Tester']='Priyanka'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)




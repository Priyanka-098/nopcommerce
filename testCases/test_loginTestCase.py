import pytest
from selenium import webdriver
from pageObjects.Test_LoginPageObject import Test_LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time


class Test_Login_TC001:

    test_base_url= ReadConfig.getBaseUrl()
    test_logintc_username=ReadConfig.getUsername()
    test_logintc_password= ReadConfig.getPassword()
    testlogger= LogGen.logsmetod()

    def test_homepage_title_validation(self,setup):

        self.testlogger.info("************Test_LoginTC/test_homepage_title_validation********")

        self.driver = setup
        self.driver.get(self.test_base_url)

        act_title= self.driver.title

        if act_title == "Your store. Login":
            assert True
            print("Homepage title validation passed")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Homepagetitle.png")
            assert False
            print("Homepage title validation failed")
            self.driver.close()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logintcmetod(self,setup):
        self.driver=setup
        self.driver.get(self.test_base_url)

        self.lpo=Test_LoginPage(self.driver)
        self.lpo.setUsername(self.test_logintc_username)
        self.lpo.setPassword(self.test_logintc_password)
        self.lpo.loginClick()
        print("login passed")


        self.driver.close()



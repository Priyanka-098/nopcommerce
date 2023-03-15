import time

from pageObjects.Test_AddCustomerPageObject import Test_AddNewCustomerPage
from pageObjects.Test_LoginPageObject import Test_LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.Test_SearchCustomerPageObject import SearchCustomerPage
import pytest


class Test_SearchCustomerbyName_TC004:

    test_base_url = ReadConfig.getBaseUrl()
    test_logintc_username = ReadConfig.getUsername()
    test_logintc_password = ReadConfig.getPassword()
    testlogger = LogGen.logsmetod()

    @pytest.mark.regression
    def test_searchCustomerbyName(self,setup):
        self.testlogger.info("********Test_SearchCustomerbyEmail/test_searchCustomerbyEmail method*********")
        self.driver = setup
        self.driver.get(self.test_base_url)
        self.driver.maximize_window()

        #Login page object class
        self.lpo = Test_LoginPage(self.driver)
        self.lpo.setUsername(self.test_logintc_username)
        self.lpo.setPassword(self.test_logintc_password)
        self.lpo.loginClick()
        self.testlogger.info("*******Test_SearchCustomerbyEmail/Login Successful msg*******")

        # Addcustomer page object class
        self.addcusto = Test_AddNewCustomerPage(self.driver)
        self.addcusto.clickCustomersmenu()
        self.addcusto.clickCustomersmenuitem()
        time.sleep(2)

        # Searchcustomer page object class
        self.testlogger.info("*******Test_SearchCustomerbyEmail/SearchCustomerbyEmail msg*******")

        self.searchcustbyname=SearchCustomerPage(self.driver)
        self.searchcustbyname.setFirstname("Victoria")
        self.searchcustbyname.setLastname("Terces")
        self.searchcustbyname.clickSearch()
        status=self.searchcustbyname.searchCustomerbyName("Victoria Terces")
        assert True== status
        self.driver.close()




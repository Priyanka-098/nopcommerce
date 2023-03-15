import pytest
import time
from pageObjects.Test_LoginPageObject import Test_LoginPage
from pageObjects.Test_AddCustomerPageObject import Test_AddNewCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import random
import string
from selenium.webdriver.common.by import By



class Test_AddnewCustomer_TC002:

    test_base_url = ReadConfig.getBaseUrl()
    test_logintc_username = ReadConfig.getUsername()
    test_logintc_password = ReadConfig.getPassword()
    testlogger = LogGen.logsmetod()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addNewCustomer(self,setup):
        self.testlogger.info("********Test_AddnewCustomer/test_addNewCustomer method*********")
        self.driver=setup
        self.driver.get(self.test_base_url)
        self.driver.maximize_window()

        self.lpo=Test_LoginPage(self.driver)
        self.lpo.setUsername(self.test_logintc_username)
        self.lpo.setPassword(self.test_logintc_password)
        self.lpo.loginClick()
        self.testlogger.info("*******Test_AddnewCustomer/Login Successful msg*******")

        self.addcusto=Test_AddNewCustomerPage(self.driver)
        self.addcusto.clickCustomersmenu()
        self.addcusto.clickCustomersmenuitem()
        self.addcusto.clickAddnew()

        self.email=random_generator() + "@gmail.com"
        self.addcusto.setEmail(self.email)
        self.addcusto.setPassword("test123")
        self.addcusto.setFirstname("john")
        self.addcusto.setLastname("math")
        self.addcusto.setGender("Male")
        self.addcusto.setDob("9/05/2000") #Forma D/MM/YYYY
        self.addcusto.setCompanyname("TCS")
        self.addcusto.checkTax()
        self.addcusto.setCustomerrole("Registered")
        self.addcusto.setManagervendor("Vendor 2")
        self.addcusto.setAdmincomment("This is 1st customer")
        self.addcusto.clickOnSave()

        self.msg= self.driver.find_element(By.TAG_NAME,"body").text
        #print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            print("New customer added successfully")
            assert True == True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"addcusomer.png")
            print("New customer added failed")
            assert False == False

        self.driver.close()


def random_generator(size=8, chars=string.ascii_lowercase +string.digits):
    return ''.join(random.choice(chars) for x in range(size))
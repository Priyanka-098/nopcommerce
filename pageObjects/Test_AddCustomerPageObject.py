from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

class Test_AddNewCustomerPage:

    lnk_Customersmenu_xpath= "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_Customers_menuitem_xpath= "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_AddNew_xpath="//a[@href='/Admin/Customer/Create']"
    txt_Email_id="Email"
    txt_Password_id="Password"
    txt_Firstname_id="FirstName"
    txt_Lastname_id="LastName"
    rd_Gendermale_id="Gender_Male"
    rd_Genderfemale_id="Gender_Female"
    txt_Dob_id="DateOfBirth"
    txt_CompanyName_id="Company"
    cb_tax_id="IsTaxExempt"
    # lst_Customerroles_xpath="//ul[@id='SelectedCustomerRoleIds_taglist']"
    lst_Customerroles_xpath="//div[@class='input-group-append input-group-required']//input[@role='listbox']"
    lstitem_Administrators_xpath="//li[text()='Administrators']"
    lstitem_ForumModerators_xpath="//li[text()='Forum Moderators']"
    lstitem_Guests_xpath="//li[text()='Guests']"
    lstitem_Registered_xpath="//li[text()='Registered']"
    lstitem_Vendors_xpath="//li[text()='Vendors']"
    drp_Managervendor_xpath="//select[@id='VendorId']"
    txt_Admincomment_xpath="//textarea[@id='AdminComment']"
    button_Save_xpath="//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomersmenu(self):
        self.driver.find_element(By.XPATH, (self.lnk_Customersmenu_xpath)).click()

    def clickCustomersmenuitem(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, (self.lnk_Customers_menuitem_xpath)).click()

    def clickAddnew(self):
        self.driver.find_element(By.XPATH, (self.btn_AddNew_xpath)).click()

    def setEmail(self,email):
        self.driver.find_element(By.ID, (self.txt_Email_id)).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID, (self.txt_Password_id)).send_keys(password)

    def setFirstname(self,firstname):
        self.driver.find_element(By.ID, (self.txt_Firstname_id)).send_keys(firstname)

    def setLastname(self,lastname):
        self.driver.find_element(By.ID, (self.txt_Lastname_id)).send_keys(lastname)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID,(self.rd_Gendermale_id)).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, (self.rd_Genderfemale_id)).click()
        else:
            self.driver.find_element(By.ID, (self.rd_Gendermale_id)).click()

    def setDob(self,dob):
        self.driver.find_element(By.ID, (self.txt_Dob_id)).send_keys(dob)

    def setCompanyname(self,companyname):
        self.driver.find_element(By.ID, (self.txt_CompanyName_id)).send_keys(companyname)

    def checkTax(self):
        self.driver.find_element(By.ID, (self.cb_tax_id)).click()

    def setCustomerrole(self,customerrole):
        self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, (self.lst_Customerroles_xpath)).click()

        if customerrole == "Registered":
            self.listitem=self.driver.find_element(By.XPATH,(self.lstitem_Registered_xpath))
        elif customerrole == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, (self.lstitem_Administrators_xpath))
        elif customerrole == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, (self.lstitem_ForumModerators_xpath))
        elif customerrole == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, (self.lstitem_Vendors_xpath))
        elif customerrole == "Guests":
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH, (self.lstitem_Guests_xpath))
        else:
            self.listitem=self.driver.find_element(By.XPATH,(self.lstitem_Registered_xpath))

        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagervendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH, (self.drp_Managervendor_xpath)))
        drp.select_by_visible_text(value)

    def setAdmincomment(self,admincomment):
        self.driver.find_element(By.XPATH, (self.txt_Admincomment_xpath)).send_keys(admincomment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, (self.button_Save_xpath)).click()










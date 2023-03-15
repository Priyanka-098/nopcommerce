import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchCustomerPage():

    txt_EmailSearch_id= "SearchEmail"
    txt_FirstnameSearch_id="SearchFirstName"
    txt_LastnameSearch_id = "SearchLastName"
    btn_Search_id="search-customers"

    #To find elements for able as we need to search in table
    table_xpath="//table[@id='customers-grid']"
    table_Rows_xpath="//table[@id='customers-grid']//tbody/tr"
    table_Columns_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.ID, (self.txt_EmailSearch_id)).clear()
        self.driver.find_element(By.ID, (self.txt_EmailSearch_id)).send_keys(email)

    def setFirstname(self,firstname):
        self.driver.find_element(By.ID, (self.txt_FirstnameSearch_id)).clear()
        time.sleep(2)
        self.driver.find_element(By.ID, (self.txt_FirstnameSearch_id)).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.ID, (self.txt_LastnameSearch_id)).clear()
        time.sleep(2)
        self.driver.find_element(By.ID, (self.txt_LastnameSearch_id)).send_keys(lastname)

    def clickSearch(self):
        self.driver.find_element(By.ID, (self.btn_Search_id)).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,(self.table_Rows_xpath)))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,(self.table_Columns_xpath)))

    def searchCustomerbyEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH, (self.table_xpath))
            emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid==email:
                flag=True
                break
        return flag

    def searchCustomerbyName(self,name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH, (self.table_xpath))
            Name=table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if Name == name:
                flag = True
                break
        return flag






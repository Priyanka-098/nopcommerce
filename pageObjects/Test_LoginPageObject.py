from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_LoginPage:
    textbox_username_id="Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[text()='Log in']"
    button_logout_xpath = "//a[text()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        self.driver.find_element(By.ID, (self.textbox_username_id)).clear()
        self.driver.find_element(By.ID,(self.textbox_username_id)).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID, (self.textbox_username_id)).clear()
        self.driver.find_element(By.ID,(self.textbox_username_id)).send_keys(password)

    def loginClick(self):
        self.driver.find_element(By.XPATH,(self.button_login_xpath)).click()

    def logoutClick(self):
        self.driver.find_element(By.XPATH,(self.button_logout_xpath_xpath)).click()




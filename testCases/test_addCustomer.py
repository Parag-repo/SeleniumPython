import pytest
import time
from pageObject.loginPage import LoginPage
from pageObject.addCustomerPage import addCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from testCases.onftest import setup

import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("********* Test_003_AddCustomer *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login successful *****")

        self.logger.info("***** Starting add customer test *****")
        self.addCust = addCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickCustomerMenuItem()

        self.addCust.clickOnAddNew()

        self.logger.info("***** Providing customer info *****")
        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Pavan")
        self.addCust.setLastName("Kumar")
        self.addCust.setGender("Male")
        self.addCust.setDob("07/05/1985")
        self.addCust.setCompanyName("busyQA")
        self.addCust.setCustomerRoles("Administrators")
        self.addCust.setManagerOfVendor("Vendor 2")
        self.addCust.setAdminContent("This is for testing....")
        self.addCust.clickOnSave()
        self.logger.info("***** Saving customer info *****")
        self.logger.info("***** Validating customer info *****")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("***** Add customer test passed *****")
        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_addCustomerScreen.png')
            self.logger.error("***** Add customer test failed *****")
            assert True == False

        self.driver.close()
        self.logger.info("***** Ending home page Title Test *****")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

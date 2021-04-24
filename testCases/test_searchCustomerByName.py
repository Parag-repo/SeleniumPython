import pytest
import time
from pageObject.loginPage import LoginPage
from pageObject.addCustomerPage import addCustomer
from pageObject.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from testCases.onftest import setup


class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_searchCustomerByName(self, setup):
        self.logger.info("********* Test_005_SearchCustomerByName *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login successful *****")

        self.logger.info("***** Starting search customer test *****")
        self.addCust = addCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickCustomerMenuItem()

        self.logger.info("***** Searching customer by Name *****")
        searchCust = SearchCustomer(self.driver)
        searchCust.setFirstName('James')
        searchCust.setLastName('Pan')
        searchCust.clickOnSearch()
        time.sleep(5)
        status = searchCust.searchCustomerByName('James Pan')
        assert True == status
        self.logger.info("***** TC_SearchCustomerByName_005_Finished *****")

        self.driver.close()

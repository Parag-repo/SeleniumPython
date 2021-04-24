import pytest
from selenium import webdriver
from pageObject.loginPage import LoginPage
from testCases.onftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********************************** Test_001_Login **********************************")
        self.logger.info(
            "********************************** Verifying Home page title **********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(3)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info(
                "********************************** Verifying Home page title test is - PASSED "
                "**********************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error(
                "********************************** Verifying Home page title test - FAILED "
                "**********************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********************************** Verifying Log in test **********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(1)
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info(
                "********************************** Verifying Log in test - PASSED **********************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error(
                "********************************** Verifying Log in test - FAILED **********************************")
            assert False

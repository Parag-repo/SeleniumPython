import time
from selenium.webdriver.support.ui import Select


class addCustomer:
    lnkCustomers_menu_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/p[1]"
    lnkCustomers_menuItem_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]" \
                                  "/li[1]/a[1]/p[1]"
    btnAddNew_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtCustomerRoles_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]" \
                             "/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]"
    lstItemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstItemForumModerator_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstItemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstItemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstItemVendors_xpath = "//li[contains(text(),'Vendors')]"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFemaleGender_xpath = "//input[@id='Gender_Female']"
    drpManagerOfVendor_xpath = "//select[@id='VendorId']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuItem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            # self.listitem = self.driver.find_element_by_xpath(self.lstItemRegistered_xpath)
            print("By default is registered")
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstItemAdministrators_xpath).click()
        elif role == 'Guest':
            time.sleep(3)
            self.driver.find_element_by_xpath("//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/span[2]").click()
            self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
            self.listitem = self.driver.find_element_by_xpath(self.lstItemGuests_xpath).click()

            time.sleep(3)
        elif role == 'Forum Moderator':
            self.listitem = self.driver.find_element_by_xpath(self.lstItemForumModerator_xpath).click()
        elif role == 'vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstItemVendors_xpath).click()
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstItemGuests_xpath).click()
        time.sleep(3)
        # self.listitem.click() - This method is not working, so we have used Java method below.
        # self.driver.execute_script("argument[0].click();", self.listitem)


    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpManagerOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()
        elif gender == 'Female':
            self.driver.find_element_by_xpath(self.rdFemaleGender_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()

    def setFirstName(self, fName):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fName)

    def setLastName(self, lName):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lName)

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()

    def setCompanyName(self, cname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(cname)
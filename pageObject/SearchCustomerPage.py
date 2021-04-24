class SearchCustomer:
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tblSearchResults_xpath = "//table[@id='customers-grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRow_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumn_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setFirstName(self, fName):
        self.driver.find_element_by_id(self.txtFirstName_id).clear()
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(fName)

    def setLastName(self, lName):
        self.driver.find_element_by_id(self.txtLastName_id).clear()
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lName)

    def clickOnSearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getNoOfRow(self):
        # return len(self.driver.find_element_by_xpath(self.tableRow_xpath))
        rowCount = 0
        for r in range(1, 1000):
            try:
                if self.driver.find_element_by_xpath("//tbody/tr[" + str(r) + "]").is_displayed():
                    rowCount = rowCount + 1
            except:
                break
        return rowCount

    def getNoOfColumn(self):
        return len(self.driver.find_element_by_xpath(self.tableColumn_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRow() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRow() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[3]").text
            if Name == name:
                flag = True
                break
        return flag

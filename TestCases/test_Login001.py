from Utilities import readconfig
from PageObject.LoginPage import LoginClass
from Utilities.readExcel import readExcel

class Test_UserLogin001:
    def test_login_001(self, setup):
        self.driver = setup
        self.ul = LoginClass(self.driver)

        filename = "D:\\CAREER\\Pytest Practice\\CredKart 2025-26\\TestData\\Login Test Credentials.xlsx"
        sheetname = "Sheet1"
        rows = readExcel.get_row_count(filename=filename, sheetname=sheetname)
        for r in range(2, rows+1):
            userEmail = readExcel.read_data(filename=filename, sheetname=sheetname, row=r, column=1)
            userPassword = readExcel.read_data(filename=filename, sheetname=sheetname, row=r, column=2)
            expected_result = readExcel.read_data(filename=filename, sheetname=sheetname, row=r, column=3)

            # Open Url
            self.driver.get(readconfig.getLoginUrl())

            # Enter Email
            # self.ul.Enter_Email(readconfig.getLoginEmail())
            self.ul.Enter_Email(userEmail)

            # Enter Password
            # self.ul.Enter_Password(readconfig.getLoginPassword())
            self.ul.Enter_Password(userPassword)

            # Click on login Button
            self.ul.ClickonLoginButton()

            # Validate login Page
            if self.ul.ValidateLoginPage() == True and expected_result == "Pass":
                print("Positive test passed...")
                assert True
            elif self.ul.ValidateLoginPage() == False and expected_result == "Fail":
                print("Negative test passed...")
                assert True
            else:
                print("Test fail (Mismatch between expected result and actual result)")
                assert False
            self.driver.delete_all_cookies()
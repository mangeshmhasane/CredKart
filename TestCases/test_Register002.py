from Utilities import readconfig
from Utilities.readExcel import readRegisterExcel
from PageObject.RegisterPage import RegisterClass

class TestRegister:
    def test_Register001(self, setup):
        self.driver = setup

        self.ur = RegisterClass(self.driver)

        filename = "D:\\CAREER\\Pytest Practice\\CredKart 2025-26\\TestData\\Register Test Data.xlsx"
        sheetname = "Sheet1"
        rows = readRegisterExcel.get_row_count(filename=filename, sheetname=sheetname)

        for r in range(2, rows+1):
            registerName = readRegisterExcel.read_data(filename=filename, sheetname=sheetname, row=r, column=1)
            registerEmail = readRegisterExcel.read_data(filename=filename, sheetname=sheetname, row=r, column=2)
            registerPassword = readRegisterExcel.read_data(filename=filename, sheetname=sheetname, row=r, column=3)
            registerConfirmPassword = readRegisterExcel.read_data(filename=filename, sheetname=sheetname, row=r, column=4)
            expectedResult = readRegisterExcel.read_data(filename=filename, sheetname=sheetname, row=r, column=5)

            # Open Url
            self.driver.get(readconfig.getRegisterUrl())

            # Enter Register Name
            self.ur.EnterRegisterName(registerName)

            # Enter Register Email
            self.ur.EnterRegisterEmail(registerEmail)

            # Enter Register Password
            self.ur.EnterRegisterPassword(registerPassword)

            # Enter Register Confirm Password
            self.ur.EnterRegisterConfirmPassword(registerConfirmPassword)

            # Click on Register Button
            self.ur.ClickonRegisterButton()

            # Validate Register Page
            if self.ur.validateRegisterPage() == True and expectedResult == "Pass":
                print("Positive Test Passed...")
                self.driver.save_screenshot(f"{readconfig.getPassscreenshotPath()}/Screenshot_Register_Pass_{r}.png")
                assert True
            elif self.ur.validateRegisterPage() == False and expectedResult == "Fail":
                print("Negative Test Passed...")
                self.driver.save_screenshot(f"{readconfig.getPassscreenshotPath()}/Screenshot_Register_Pass_{r}.png")
                assert True
            else:
                print("Test Failed: (Expected Result and Actual Result Mismatched...)")
                self.driver.save_screenshot(f"{readconfig.getFailscreenshotPath()}/Screenshot_Register_Fail_{r}.png")
                assert False
            self.driver.delete_all_cookies()
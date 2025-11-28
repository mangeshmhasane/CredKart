from Utilities import readconfig
from PageObject.LoginPage import LoginClass
from Utilities.readExcel import readLoginExcel
from Utilities.logger import get_logger

class Test_UserLogin001:
    def test_login_002(self, setup):
        self.driver = setup
        self.ul = LoginClass(self.driver)
        logger = get_logger()
        logger.info("Test Started: test_test_login001")
        
        filename = "D:\\CAREER\\Pytest Practice\\CredKart 2025-26\\TestData\\Login Test Credentials.xlsx"
        sheetname = "Sheet1"
        rows = readLoginExcel.get_row_count(filename=filename, sheetname=sheetname)
        for r in range(2, rows+1):
            userEmail = readLoginExcel.read_data(filename=filename, sheetname=sheetname, row=r, column=1)
            userPassword = readLoginExcel.read_data(filename=filename, sheetname=sheetname, row=r, column=2)
            expected_result = readLoginExcel.read_data(filename=filename, sheetname=sheetname, row=r, column=3)

            # Open Url
            self.driver.get(readconfig.getLoginUrl())
            logger.info("Opened URL")

            # Enter Email
            self.ul.Enter_Email(userEmail)
            logger.info("Entered UserEmail")

            # Enter Password
            self.ul.Enter_Password(userPassword)
            logger.info("Entered UserPassword")

            # Click on login Button
            self.ul.ClickonLoginButton()
            logger.info("Clicked Login Button")

            # Validate login Page
            if self.ul.ValidateLoginPage() == True and expected_result == "Pass":
                print(f"Positive test_{r-1} passed...")
                logger.info(f"Posite Test_{r-1} Passed: Login Successful")
                self.driver.save_screenshot(f"{readconfig.getPassscreenshotPath()}/Screenshot_Test_Login_Passed_{r-1}.png")
                assert True
            elif self.ul.ValidateLoginPage() == False and expected_result == "Fail":
                print(f"Negative test_{r-1} passed...")
                logger.info(f"Negative Test_{r-1} Passed: Login Successful")
                self.driver.save_screenshot(f"{readconfig.getPassscreenshotPath()}/Screenshot_Test_Login_Passed_{r-1}.png")
                assert True
            else:
                print(f"Test_{r-1} fail (Mismatch between expected result and actual result)")
                logger.info(f"Test_{r-1} Failed: Login Unsuccessful")
                self.driver.save_screenshot(f"{readconfig.getFailscreenshotPath()}/Screenshot_Test_Login_Failed_{r-1}.png")
                assert False
            self.driver.delete_all_cookies()
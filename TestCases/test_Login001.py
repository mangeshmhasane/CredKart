from Utilities import readconfig
from PageObject.LoginPage import LoginClass

class Test_UserLogin001:
    def test_login_001(self, setup):
        self.driver = setup
        self.ul = LoginClass(self.driver)

        # Open Url
        self.driver.get(readconfig.getLoginUrl())

        # Enter Email
        self.ul.Enter_Email(readconfig.getLoginEmail())

        # Enter Password
        self.ul.Enter_Password(readconfig.getLoginPassword())

        # Click on login Button
        self.ul.ClickonLoginButton()

        # Validate login Page
        try:
            self.ul.ValidateLoginPage()
            print("Login Successful...")
            assert True
        except:
            print("Error: Login Unsuccessful...")
            assert False
        
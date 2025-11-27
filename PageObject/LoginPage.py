from selenium.webdriver.common.by import By

class LoginClass:
    loginEmailID = (By.ID, "email")
    loginPasswordID = (By.ID, "password")
    LoginButtonXPATH = (By.XPATH, "//button[@type = 'submit']")
    LoginValidationXPATH = (By.XPATH, "//h2[text() = 'CredKart']")

    def __init__(self, driver):
        self.driver = driver

    def Enter_Email(self, email):
        self.driver.find_element(*LoginClass.loginEmailID).send_keys(email)
    
    def Enter_Password(self, password):
        self.driver.find_element(*LoginClass.loginPasswordID).send_keys(password)
    
    def ClickonLoginButton(self):
        self.driver.find_element(*LoginClass.LoginButtonXPATH).click()
    
    def ValidateLoginPage(self):
        try:
            self.driver.find_element(*LoginClass.LoginValidationXPATH)
            return True
        except:
            return False
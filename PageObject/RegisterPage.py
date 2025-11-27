from selenium.webdriver.common.by import By

class RegisterClass:
    registerNameID = (By.ID, "name")
    registerEmailID = (By.ID, "email")
    registerPasswordID = (By.ID, "password")
    registerConfirmPasswordID = (By.ID, "password-confirm")
    registerButtonXPATH = (By.XPATH, "//button[@type = 'submit']")
    validateRegisterPage = (By.XPATH, "//h2[text() = 'CredKart']")

    def __init__(self, driver):
        self.driver = driver

    def EnterRegisterName(self, name):
        self.driver.find_element(*RegisterClass.registerNameID).send_keys(name)

    def EnterRegisterEmail(self, Email):
        self.driver.find_element(*RegisterClass.registerEmailID).send_keys(Email)
    
    def EnterRegisterPassword(self, Password):
        self.driver.find_element(*RegisterClass.registerPasswordID).send_keys(Password)
    
    def EnterRegisterConfirmPassword(self, Confirm_password):
        self.driver.find_element(*RegisterClass.EnterRegisterConfirmPassword).send_keys(Confirm_password)
    
    def ClickonRegisterButton(self):
        self.driver.find_element(*RegisterClass.registerButtonXPATH).click()
    
    def validateRegisterPage(self):
        try:
            self.driver.find_element(*RegisterClass.validateRegisterPage)
            return True
        except:
            return False
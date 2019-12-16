from appium import webdriver


class StartSettings(object) :
    def __init__(self, driver):
        self.driver = driver

    def ClickOnAllowButton(self):
        self.driver.find_element_by_xpath("//android.widget.Button[@text = 'ALLOW']").click()

    def ContinueWithPhoneNumber(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text = 'Continue with Phone Number']").click()

    def EnterPhoneNumber ( self, phonenumber):
        self.driver.find_element_by_xpath("//android.widget.EditText[@text = 'Mobile Number']").send_keys(phonenumber)
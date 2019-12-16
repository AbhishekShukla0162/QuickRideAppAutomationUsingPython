from appium import webdriver


class BookRide(object) :
    def __init__(self, driver):
        self.driver = driver

    def ClickOnCurrentLocation(self):
        self.driver.find_element_by_id("com.disha.quickride:id/tv_from_location").click()

    def ChooseCurrentLocation(self , startPoint):
        self.driver.find_element_by_xpath("//android.widget.EditText[@text = 'Enter from location']").send_keys(startPoint)

    def SelectStartLocation ( self ) :
        self.driver.find_element_by_xpath("//android.widget.TextView[@text = 'Yelahanka, Bengaluru, Karnataka, India']").click()

    def ClickOnRidelocation ( self ) :
        self.driver.find_element_by_id("com.disha.quickride:id/tv_to_location").click()

    def ChooseRideLocation ( self, EndPoint ) :
        self.driver.find_element_by_xpath("//android.widget.EditText[@text = 'Enter to location']").send_keys(EndPoint)

    def SelectEndLocation ( self ) :
        self.driver.find_element_by_xpath("//android.widget.TextView[@text = 'Mother Dairy']").click()

    def ClickFindRide ( self ) :
        self.driver.find_element_by_id("//android.widget.Button[@text = 'FIND RIDE']").click()

    def JoinARide ( self ) :
        self.driver.find_element_by_xpath("//android.widget.TextView[@text = 'Join']").click()

    def VerifyYourRide ( self ) :
        self.driver.find_element_by_xpath("//android.widget.Button[@text = 'VERIFY NOW']").click()
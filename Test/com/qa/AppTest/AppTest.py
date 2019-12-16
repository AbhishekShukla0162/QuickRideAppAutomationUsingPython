import os
import sys
import time
import unittest

from appium import webdriver
from Main.com.qa.AppPages.StartPage import StartSettings
from Main.com.qa.AppPages.RideBookingPage import BookRide

sys.path.append(os.path.realpath(os.getcwd()))


class RunAppLoginTest(unittest.TestCase) :
    def setUp ( self ) :
        desired_caps = {
            "platformName" : "Android",
            "platformVersion" : "10.0",
            "deviceName" : "Android Device",
            "automationName" : "UiAutomator2",
            "app" : "/Users/manish/Documents/QuickRideAppPythonAutomation/QuickRideAppAutomationUsingPython/AppTestData/Quick Ride.com.apk"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_FirstDemo ( self ) :
        time.sleep(5)
        driver = self.driver
        time.sleep(5)

        settings = StartSettings(driver)
        time.sleep(3)

        settings.ClickOnAllowButton()
        settings.ContinueWithPhoneNumber()
        settings.EnterPhoneNumber("8565009444")

        rideBooking = BookRide(driver)

        rideBooking.ClickOnCurrentLocation()
        rideBooking.ChooseCurrentLocation("Yelahanka New Town, Bengaluru, Karnataka 560064")
        rideBooking.SelectStartLocation()
        rideBooking.ClickOnRidelocation()
        rideBooking.ChooseRideLocation("Near Prestige Mall, Udaya Layout, Yelahanka New Town, Bengaluru, Karnataka 560064")
        rideBooking.SelectEndLocation()
        rideBooking.ClickFindRide()
        rideBooking.JoinARide()
        rideBooking.VerifyYourRide()
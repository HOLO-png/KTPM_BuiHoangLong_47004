import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.signupPage import signupPage
from pages.homePage import homePage
from utillities.customLogger import Loggen
from utillities.readproperty import ReadConfig
import time

baseURL = ReadConfig.getURL()
mylogger = Loggen.loggen()


@given(u'Launch the App Signup')
def step_impl(context):
    context.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    mylogger.info("****Driver Signup Initialized ****")
    context.driver.get(baseURL)
    mylogger.info("****Browser Signup Launched ****")


@when(u'enter Signup credentials')
def step_impl(context):
    mylogger.info("****Passing Signup Credentials ****")
    global hpage
    global spage
    hpage = homePage(context.driver)
    hpage.clickOnSignup()
    spage = signupPage(context.driver)
    usr = ReadConfig.getUserName()
    eml = ReadConfig.getEmailSignup()
    pwd = ReadConfig.getPassword()
    time.sleep(2)
    spage.setusername(usr)
    spage.setemail(eml)
    spage.setpassword(pwd)
    mylogger.info("**** Entered Signup Credentials ****")


@then(u'accept cookie notification')
def step_impl(context):
    spage.acceptCookie()
    mylogger.info("**** accept cookie notification ****")
    time.sleep(1)


@then(u'validate signup form')
def step_impl(context):
    spage.checkValidateSignupForm()
    mylogger.info("****check validate form Signup ****")
    time.sleep(7)


@then(u'click signup')
def step_impl(context):
    spage.clickOnSignup()
    mylogger.info("****Clicked Signup Button ****")
    time.sleep(3)


@then(u'verify the page title and screenshot Signup')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = "Confirmation"
    if actual_title == expected_title:
        assert True
        context.driver.save_screenshot(
            "C:\\Users\\Admin\\PycharmProjects\\pythonProject\\screenShots\\" + "SignupPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="c2ta Signup test",
                      attachment_type=AttachmentType.PNG)
        mylogger.info("****Title Signup matched****")
    else:
        mylogger.info("****Title Signup not matched****")
        context.driver.save_screenshot(
            "C:\\Users\\Admin\\PycharmProjects\\pythonProject\\screenShots" + "SignupPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="c2ta Signup test",
                      attachment_type=AttachmentType.PNG)
        assert False
    time.sleep(2)


@then(u'close the App Signup')
def step_impl(context):
    context.driver.close()
    mylogger.info("****Browser Signup closed****")
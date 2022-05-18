import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.loginPage import LoginPage
from utillities.customLogger import Loggen
from utillities.readproperty import ReadConfig
import time
from utillities import XLDataExcel


baseURL = ReadConfig.getURLLogin()
mylogger = Loggen.loggen()
pathExcel = ReadConfig.getPathExcel()
sheetLogin = ReadConfig.getSheetLogin()


@given(u'Launch the App')
def step_impl(context):
    context.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    mylogger.info("****Driver Initialized ****")
    context.driver.get(baseURL)
    cookie_cta = context.driver.find_element_by_id('accept-cookie-notification')
    cookie_cta.click()
    mylogger.info("****Browser Launched ****")


@when(u'Enter login credentials')
def step_impl(context):
    mylogger.info("****Passing Credentials ****")
    global hpage
    global lpage
    lpage = LoginPage(context.driver)
    rows = XLDataExcel.getRowCount(pathExcel, sheetLogin)
    for r in range(2, rows+1):
        email = XLDataExcel.readData(pathExcel, sheetLogin, r, 1)
        password = XLDataExcel.readData(pathExcel, sheetLogin, r, 2)
        lpage.setusername(email)
        lpage.setpassword(password)
        lpage.clickOnLogin()
        txt1 = "****Entered Credentials {} passed *****"
        txt2 = "****Entered Credentials {} failed *****"
        time.sleep(4)
        if context.driver.current_url == "https://live.browserstack.com/dashboard#os=android&os_version=9.0&device=Google+Pixel+3&device_browser=chrome&zoom_to_fit=true&full_screen=true&url=https%3A%2F%2Ftechcrunch.com%2F&speed=1":
            mylogger.info(txt1.format(r-1))
            XLDataExcel.writeData(pathExcel, sheetLogin, r, 3, "test passed")
            context.driver.back()
        else:
            mylogger.info(txt2.format(r-1))
            XLDataExcel.writeData(pathExcel, sheetLogin, r, 3, "test failed")

        context.driver.refresh()
    mylogger.info("****Entered Credentials end ****")


@then(u'Screenshot login')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = "Dashboard"
    if actual_title == expected_title:
        assert True
        context.driver.save_screenshot(
            "C:\\Users\\Admin\\PycharmProjects\\pythonProject\\screenShots\\" + "LoginPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="c2ta LoginPage test",
                      attachment_type=AttachmentType.PNG)
        mylogger.info("****Title LoginPage matched****")
    else:
        mylogger.info("****Title LoginPage not matched****")
        context.driver.save_screenshot(
            "C:\\Users\\Admin\\PycharmProjects\\pythonProject\\screenShots" + "LoginPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="c2ta LoginPage test",
                      attachment_type=AttachmentType.PNG)
        assert False
    time.sleep(2)


@then(u'Handle logout')
def step_impl(context):
    lpage.clickOnSignOut()
    time.sleep(1)
    mylogger.info("****Handle logout success****")


@then(u'Close the App')
def step_impl(context):
    context.driver.close()
    mylogger.info("****Browser closed****")

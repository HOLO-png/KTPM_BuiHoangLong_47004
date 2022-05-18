from behave import *
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utillities.customLogger import Loggen
from utillities.readproperty import ReadConfig
import time

baseURL = ReadConfig.getURL()
mylogger = Loggen.loggen()


@given(u'Launch the browser')
def step_impl(context):
    context.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    mylogger.info("****Driver Initialized ****")
    context.driver.get(baseURL)
    mylogger.info("****Browser Launched ****")


@then(u'verify the page title')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = "Most Reliable App & Cross Browser Testing Platform | BrowserStack"
    if actual_title == expected_title:
        assert True
        mylogger.info("****Title matched****")
    else:
        mylogger.info("****Title not matched****")
        assert False
        time.sleep(5)


@then(u'close the browser')
def step_impl(context):
    context.driver.close()
    mylogger.info("****Browser closed****")

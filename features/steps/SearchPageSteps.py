from behave import *
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utillities import XLDataExcel
from utillities.customLogger import Loggen
from utillities.readproperty import ReadConfig
from pages.homePage import homePage
import time


baseURL = ReadConfig.getURL()
mylogger = Loggen.home()
pathExcel = ReadConfig.getPathExcel()
sheetSearch = ReadConfig.getSheetSearch()


@given(u'Launch the browser search')
def step_impl(context):
    context.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    mylogger.info("****Driver search Initialized ****")
    context.driver.get(baseURL)
    mylogger.info("****Browser search Launched ****")


@when(u'identify search box & enter search text')
def step_impl(context):
    global hpage
    hpage = homePage(context.driver)
    rows = XLDataExcel.getRowCount(pathExcel, sheetSearch)
    hpage.clickOnOpenInputSearch()
    list_item = '//*[@id="all-search-ds-results"]/div/div'

    for r in range(2, rows+1):
        actual_title = context.driver.title
        keysSearch = XLDataExcel.readData(pathExcel, sheetSearch, r, 1)
        keysSearch2 = XLDataExcel.readData(pathExcel, sheetSearch, r-1, 1)
        expected_title = "Search Results for {}"

        mylogger.info(expected_title.format(keysSearch2))
        mylogger.info(actual_title)

        if actual_title == expected_title.format(keysSearch2):
            hpage.clickOnOpenInputSearch2()

        hpage.setInputSearchText(keysSearch)
        hpage.clickOnSearchKeys()
        txt1 = "****Search keys {} passed *****"
        txt2 = "****Search keys {} failed *****"
        time.sleep(3)
        listElement = context.driver.find_element_by_xpath(list_item)

        mylogger.info(listElement.get_attribute("class"))

        if listElement.get_attribute("class") == "ais-Hits":
            mylogger.info(txt1.format(r-1))
            XLDataExcel.writeData(pathExcel, sheetSearch, r, 2, "test passed")
        else:
            mylogger.info(txt2.format(r-1))
            XLDataExcel.writeData(pathExcel, sheetSearch, r, 2, "test failed")

    mylogger.info("****Entered Credentials end ****")


@then(u'check title and screenShots search')
def step_impl(context):
    hpage.scrollSearchPage()
    context.driver.save_screenshot(
        "C:\\Users\\Admin\\PycharmProjects\\pythonProject\\screenShots\\" + "search.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="c2ta Search test",
                  attachment_type=AttachmentType.PNG)
    mylogger.info("****title screen search matched ****")
    time.sleep(2)


@then(u'close the browser search')
def step_impl(context):
    context.driver.close()
    mylogger.info("**** Browser search closed****")

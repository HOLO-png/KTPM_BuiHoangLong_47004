import time


class homePage:
    icon_search_xpath = "//header/div[1]/div[1]/nav[1]/ul[1]/li[10]/button[1]"
    txt_input_search_id = "doc-search-box-input"
    btn_input_search_xpath = '//*[@id="ds-input-handle"]/button[2]'
    item_search_xpath = '//*[@id="all-search-ds-results"]/div/div/ol/li[1]/div/a'
    icon_search_xpath2 = '//*[@id="doc-menu-toggle"]'

    def __init__(self, driver):
        self.driver = driver
        self.link_login_id = "signupModalButton"

    def clickOnSignup(self):
        button = self.driver.find_element_by_id('signupModalButton')
        button.click()

    # search functionally

    def setInputSearchText(self, keyword):
        for character in keyword:
            self.driver.find_element_by_id(self.txt_input_search_id).send_keys(character)
            time.sleep(0.1)

    def clickOnOpenInputSearch(self):
        self.driver.find_element_by_xpath(self.icon_search_xpath).click()

    def clickOnOpenInputSearch2(self):
        self.driver.find_element_by_xpath(self.icon_search_xpath2).click()

    def clickOnSearchKeys(self):
        self.driver.find_element_by_xpath(self.btn_input_search_xpath).click()

    def scrollSearchPage(self):
        self.driver.find_element_by_xpath(self.item_search_xpath).click()

    def checkDataSearchListIsEnable(self):
        self.driver.find_element_by_xpath(self.item_search_xpath).click()


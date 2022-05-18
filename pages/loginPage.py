import time
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage:
    txt_username_id = "user_email_login"
    txt_password_id = "user_password"
    btn_login_xpath = "//input[@id='user_submit']"
    link_signup_xpath = "//body/main[1]/div[4]/section[1]/form[1]/div[1]/div[1]/div[1]/div[11]/div[1]/a[1]"
    link_sign_out_xpath = "//a[@id='sign_out_link']"
    btn_user_xpath = "/html/body/div[1]/header/div/div/nav/ul[1]/li[7]/button"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, usrname):
        for character in usrname:
            self.driver.find_element_by_id(self.txt_username_id).send_keys(character)
            time.sleep(0.1)

    def setpassword(self, password):
        for character in password:
            self.driver.find_element_by_id(self.txt_password_id).send_keys(character)
            time.sleep(0.1)

    def clearInput(self):
        self.driver.find_element_by_id(self.txt_username_id).clear()
        self.driver.find_element_by_id(self.txt_password_id).clear()

    def clickOnLogin(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()

    def clickOnSignOut(self):
        a = ActionChains(self.driver)
        m = self.driver.find_element_by_xpath(self.btn_user_xpath)
        a.move_to_element(m).perform()
        n = self.driver.find_element_by_xpath(self.link_sign_out_xpath)
        a.move_to_element(n).click().perform()

    def clickOnSignup(self):
        self.driver.find_element_by_xpath(self.link_signup_xpath).click()

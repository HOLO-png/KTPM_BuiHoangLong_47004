import time
from utillities.customLogger import Loggen

BASE_URL = "https://www.browserstack.com"
EMAIL_ID = "<your email ID>"
EXPECTED_COLOR = "rgba(222, 20, 33, 1)"

mylogger = Loggen.loggen()


class signupPage:
    txt_username_id = "user_full_name"
    txt_email_id = "user_email_login"
    txt_password_id = "user_password"
    btn_signup_xpath = "//input[@id='user_submit']"
    terms_and_conditions_name = "terms_and_conditions"
    capchar_id = "accept-cookie-notification"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, usrname):
        for character in usrname:
            self.driver.find_element_by_id(self.txt_username_id).send_keys(character)
            time.sleep(0.2)

    def setemail(self, email):
        for character in email:
            self.driver.find_element_by_id(self.txt_email_id).send_keys(character)
            time.sleep(0.2)

    def setpassword(self, password):
        for character in password:
            self.driver.find_element_by_id(self.txt_password_id).send_keys(character)
            time.sleep(0.2)

    def clickOnTermsAndConditions(self):
        self.driver.find_element_by_name(self.terms_and_conditions_name).click()

    def clickOnSignup(self):
        self.driver.find_element_by_xpath(self.btn_signup_xpath).click()

    def acceptCookie(self):
        self.driver.find_element_by_id(self.capchar_id).click()

    def checkValidateSignupForm(self):
        username = self.driver.find_element_by_id('user_full_name')
        if "error" in username.get_attribute('outerHTML'):
            obtained_color = username.value_of_css_property('border-bottom-color')
            if not self.checkColor(obtained_color, "rgba(222, 20, 33, 1)"):
                mylogger.info(f"[user_full_name] expected color is {EXPECTED_COLOR} and got {obtained_color}")

        email = self.driver.find_element_by_id('user_email_login')
        if "error" in email.get_attribute('outerHTML'):
            obtained_color = email.value_of_css_property('border-bottom-color')
            if not self.checkColor(obtained_color, "rgba(222, 20, 33, 1)"):
                mylogger.info(f"[user_email_login] expected color is {EXPECTED_COLOR} and got {obtained_color}")

        password = self.driver.find_element_by_id('user_password')
        if "error" in password.get_attribute('outerHTML'):
            obtained_color = password.value_of_css_property('border-bottom-color')
            if not self.checkColor(obtained_color, "rgba(222, 20, 33, 1)"):
                mylogger.info(f"[user_password] expected color is {EXPECTED_COLOR} and got {obtained_color}")

        error_messages = ["At least 3 characters",
                          "Invalid Email", "At least 6 characters"]
        message_body_html_elements = self.driver.find_elements_by_class_name('msg-body')
        for msg in message_body_html_elements:
            error_msg = msg.get_attribute('innerHTML').split("span")[1][1:-2]
            if error_msg not in error_messages:
                mylogger.info(f"{msg.get_attribute('outerHTML')} is missing error message")

    @staticmethod
    def checkColor(color, orginal_color):
        return color == orginal_color

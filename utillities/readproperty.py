import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\Admin\\PycharmProjects\\pythonProject\\configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get("common-info", "baseURL")
        return url

    @staticmethod
    def getUserName():
        username = config.get("common-info", "userName")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common-info", "password")
        return password

    @staticmethod
    def getEmailSignup():
        email = config.get("common-info", "email-signup")
        return email

    @staticmethod
    def getURLLogin():
        urlLogin = config.get("common-info", "baseURLLogin")
        return urlLogin

    @staticmethod
    def getKeyWord():
        keyWord = config.get("common-info", "keyWord")
        return keyWord

    @staticmethod
    def getEmailSignin():
        keyWord = config.get("common-info", "email-signin")
        return keyWord

    @staticmethod
    def getPathExcel():
        pathExcel = config.get("common-info", "pathExcel")
        return pathExcel

    @staticmethod
    def getSheetLogin():
        sheet = config.get("common-info", "sheetLogin")
        return sheet

    @staticmethod
    def getSheetSearch():
        sheet = config.get("common-info", "sheetSearch")
        return sheet



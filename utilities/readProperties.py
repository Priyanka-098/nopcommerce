import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getBaseUrl():
        url= config.get("Login Details", "conf_base_url")
        return url

    @staticmethod
    def getUsername():
        un= config.get("Login Details", "conf_logintc_username")
        return un

    @staticmethod
    def getPassword():
        pwd= config.get("Login Details","conf_logintc_password")
        return pwd
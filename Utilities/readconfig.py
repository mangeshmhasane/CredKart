import configparser
configPath = "D:\\CAREER\\Pytest Practice\\CredKart 2025-26\\Configuration\\config.ini"
config = configparser.ConfigParser()
config.read(configPath)

@staticmethod
def getLoginUrl():
    return config['user info']['LoginUrl']

@staticmethod
def getLoginEmail():
    return config['user info']['LoginEmail']

@staticmethod
def getLoginPassword():
    return config['user info']['LoginPassword']

@staticmethod
def  getRegisterUrl():
    return config['user info']['RegisterUrl']
import configparser
configPath = "D:\\CAREER\\Pytest Practice\\CredKart 2025-26\\1. Configuration\\config.ini"
config = configparser.ConfigParser()
config.read(configPath)

@staticmethod
def getLoginUrl():
    config['user info']['LoginUrl']

@staticmethod
def getLoginEmail():
    config['user info']['LoginEmail']

@staticmethod
def getLoginPassword():
    config['user info']['LoginPassword']
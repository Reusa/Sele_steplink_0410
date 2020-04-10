from selenium import webdriver

browser = webdriver.Chrome()
#browser.get('http://www.baidu.com')

config1 = "config.ini"
conf = ConfigParser.ConfigParser()
conf.read(config1)

print(conf.get("browserType","browserName"))
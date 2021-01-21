from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')

def searching_company(name):
    driver.get('https://naver.com')

    sel = "#query"
    ui = driver.find_element_by_css_selector(sel)
    ui.send_keys(name)
    ui.send_keys(Keys.RETURN)

searching_company("패스트캠퍼스")
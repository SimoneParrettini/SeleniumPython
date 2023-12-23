from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def test_execute():
                    driver = Chrome()
                    driver.get("https://www.theTestingWorld.com/testings/")
                    driver.find_element(By.NAME,"fld_username").send_keys("Hello")

                    act = ActionChains(driver)
                    act.key_down(Keys.CONTROL).send_keys('a').perform()
                    time.sleep(10)
                    #while(True):
                     #pass
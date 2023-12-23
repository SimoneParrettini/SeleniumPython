from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def test_execute():
                    driver = Chrome()
                    driver.get("https://www.thetestingworld.com")

                    act = ActionChains(driver)

                    # Click Operations
                    #act.click().perform()
                    #act.click(driver.find_element(By.XPATH,"//a[text()='Quick Demo']")).perform()

                    # Context Click Operations
                    #act.context_click().perform()
                    #act.context_click(driver.find_element(By.XPATH,"//a[text()='Quick Demo']")).perform()

                    #Double Click Operations
                    #act.double_click().perform()
                    #act.double_click(driver.find_element(By.XPATH,"//a[text()='Quick Demo']")).perform()

                    act.move_to_element(driver.find_element(By.XPATH,"//span[contains(text(),'TUTORIAL')]")).perform()
                    act


                    #while(True):
                     #pass
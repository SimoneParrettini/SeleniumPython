from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
import time
import pytest

@pytest.fixture()
def environment_setup():
    global driver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.thetestingworld.com/testings/")
    driver.maximize_window()
    yield
    driver.close()


def test_verify_registration(environment_setup):


            obj = Select(driver.find_element(By.ID,"countryId"))
            obj.select_by_visible_text("India")

            wait = WebDriverWait(driver, 100)
            wait.until(ec.text_to_be_present_in_element((By.ID,'stateId'),"Delhi" ))
            obj = Select(driver.find_element(By.ID, "stateId"))
            obj.select_by_visible_text("Delhi")

            time.sleep(10)

            driver.find_element(By.XPATH,"//input[@value='office']").click()

            driver.find_element(By.NAME,"terms").click()

            driver.find_element(By.XPATH,"//input[@type='submit']").click()

            driver.find_element(By.LINK_TEXT,"Read Detail").click()

            # Fetch selected option

            #print(obj.first_selected_option.text)

            #print("*******************************************")
            #for op in obj.options:
            # print(op.text)

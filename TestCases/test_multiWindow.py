from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import time
import pytest

@pytest.fixture()
def environment_setup():
    global driver
    driver=Chrome()
    driver.get("https://www.thetestingworld.com/testings/")
    driver.maximize_window()
    yield
    driver.close()


def test_verify_registration(environment_setup):
    driver.find_element(By.XPATH,"//label[text()='Login']").click()
    driver.find_element(By.NAME,"_txtUserName").send_keys('testparrettini')
    driver.find_element(By.NAME,"_txtPassword").send_keys('testparrettini')
    driver.find_element(By.XPATH,"//input[@type='submit' and @value='Login']").click()
    driver.find_element(By.XPATH,"//a[(contains(text(),'My Account'))]").click()
    driver.find_element(By.XPATH,"//a[(contains(text(),'Update'))]").click()
    time.sleep(10)
    allwindows = driver.window_handles
    print(allwindows)
    mainWin=""

    for win in allwindows:
        driver.switch_to.window(win)
        print(driver.current_url)
        if (driver.current_url=='https://www.thetestingworld.com/testings/manage_customer.php'):
            driver.find_element(By.XPATH,"//button[text()='Start Download']").click()
            time.sleep(5)
            driver.close()
        elif (driver.current_url=='https://www.thetestingworld.com/testings/dashboard.php'):
            mainWin=win


        driver.switch_to.window(mainWin)
        print(driver.current_url)












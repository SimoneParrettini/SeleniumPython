from time import sleep


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_execute():
                  options=webdriver.FirefoxOptions()
                  driver = webdriver.Firefox(options=options)
                  driver.get("https://www.thetestingworld.com/testings/")

                  #maximize_window
                  driver.maximize_window()

                  #enter data to text box
                  driver.find_element(By.NAME,'fld_username').send_keys('helloworld')
                  driver.find_element(By.XPATH,"//input[@name='fld_email']").send_keys('testingworldindia@gmail.com')
                  driver.find_element(By.NAME,'fld_password').send_keys('abcd123')
                  driver.find_element(By.NAME,'fld_cpassword').send_keys('abcd123')
                  driver.find_element(By.NAME,'fld_username').clear()
                  driver.find_element(By.NAME,'fld_username').send_keys('abcd123')

                  # Working on Radio button
                  #driver.find_element(By.XPATH,"//input[@value='home']").click()
                  driver.find_element(By.XPATH,"//input[@value='office']").click()

                  # Work on dropdown list
                  obj = Select(driver.find_element(By.NAME,"sex"))
                  #obj.select_by_visible_text("Male")
                  #obj.select_by_value("2")
                  #obj.select_by_index(2)

                  # Working on Checkbox
                  driver.find_element(By.NAME,'terms').click()

                  #Work on button
                  #driver.find_element(By.XPATH,"//input[@type='submit']").click()

                  # Work on links
                  driver.find_element(By.LINK_TEXT,"Read Detail").click()
                  driver.find_element(By.CLASS_NAME,"close").click()

                  # Work on dropdown list

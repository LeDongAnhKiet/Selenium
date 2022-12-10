from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.facebook.com/')
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//*[text()='Create New Account']").click()
driver.find_element(By.NAME, "firstname").send_keys("kiet")
driver.find_element(By.NAME, "lastname").send_keys("lê đông")
driver.find_element(By.NAME, "reg_email__").send_keys("lekiet@gmail.com")
day = Select(driver.find_element(By.ID, "day"))
day.select_by_index("1")
month = Select(driver.find_element(By.ID, "month"))
month.select_by_visible_text("Feb")
year = Select(driver.find_element(By.ID, "year"))
year.select_by_index("3")
driver.find_element(By.XPATH, "//label[text()='Male']").click()
driver.find_element(By.NAME, "websubmit").click()

driver.close()

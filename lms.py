from selenium import webdriver
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://lms.ou.edu.vn/')

driver.find_element(By.CLASS_NAME, 'main-btn').click()
driver.find_element((By.CLASS_NAME, 'login100-from-btn')).click()

u = Select(driver.find_element(By.NAME, 'form-usertype'))
u.select_by_index(0)

with open('test.csv', 'r', newline='') as f:
    r = csv.DictReader(f)
    for row in r:
        user = row['user']
        password = row['password']
driver.find_element(By.CSS_SELECTOR, 'm-loginbox-submit-btn').click()

course = driver.find_elements(By.CSS_SELECTOR, '.dashboard-card-deck .dashboard-card')
for c in course:
    print(c.text)

driver.close()
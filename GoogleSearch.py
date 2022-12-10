from selenium import webdriver
from selenium.webdriver.common.by import By

driv = webdriver.Chrome(executable_path='chromedriver.exe')
driv.get('https://www.google.com')
s = input('Nhập: ')
ctrl = driv.find_element(By.NAME, 'q')
ctrl.send_keys(s)
ctrl.submit()

res = driv.find_elements(By.CSS_SELECTOR, 'div.g')
a = 1
for r in res:
    t = r.find_element(By.TAG_NAME, 'a').text
    l = r.find_element(By.TAG_NAME, 'a').get_attribute('href')
    a += 1
    print(t + '\n' + l + '\n')
    if a > 5:
        break

driv.close()

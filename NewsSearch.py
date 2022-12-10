from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://vnexpress.net/')

articles = driver.find_elements(By.CSS_SELECTOR, 'article.item-news')
count = 0
for a in articles:
    try:
        title = a.find_element(By.CSS_SELECTOR, 'h3.title-news').text
        desc = a.find_element(By.TAG_NAME, 'p').text
        link = a.find_element(By.CSS_SELECTOR, 'h3.title-news > a').get_attribute('href')
        print(title + '\n' + desc + '\n' + link)
        count += 1
        if count > 20:
            break
    except NoSuchElementException:
        # print('lỗi')
        continue

driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 在这里写入你的账户和密码
your_id = 'xxxx'
your_password = 'xxxx'
url = 'https://sso.tju.edu.cn/cas/login?service=http%3A%2F%2Fclasses.tju.edu.cn%2Feams%2FhomeExt.action%3Bjsessionid%3D72E4CE82C1D32601B7545E6DB2E3399E.std3'

options = webdriver.ChromeOptions()
options.add_argument('--disable-infobars')

browser = webdriver.Chrome(options = options)
browser.get(url)

id = browser.find_element(by=By.ID, value="un")
psd = browser.find_element(by=By.ID, value="pd")
id.clear()
psd.clear()
id.send_keys(your_id)
psd.send_keys(your_password)
time.sleep(5)
login_button = browser.find_element(by=By.CLASS_NAME, value="login-btn")
login_button.click()
time.sleep(3)

button = browser.find_element(By.PARTIAL_LINK_TEXT, "量化评教")
button.click()
button = browser.find_element(By.PARTIAL_LINK_TEXT, "学生评教")
button.click()
time.sleep(0.5)

browser.switch_to.frame("iframeMain")
while True:
    try:
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "eval")))
        button.click()
        time.sleep(0.5)
        elements = browser.find_elements(By.XPATH, '//*[@value="4"]')
        for element in elements:
            element.click()
        time.sleep(0.5)
        # elements = browser.find_elements(By.CLASS_NAME, "answer answer-textarea")
        elements = browser.find_elements(By.XPATH, '//*[contains(@class, "answer-textarea")]')
        for element in elements:
            element.clear()
            element.send_keys("none")
        time.sleep(1)
        element = browser.find_element(By.ID, "sub")
        element.click()
        alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
        alert.accept()
        time.sleep(1.5)
    except Exception:
        browser.quit()
        print("Done!")
        break

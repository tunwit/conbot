from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import json

with open('config.json','r',encoding='utf-8') as json_file:
    data = json.load(json_file)

assert True        
options = Options()
options.add_experimental_option('detach', True)

username = data['username']
password = data['password']

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

driver.get('https://www.thaiticketmajor.com/index.html')

#accept cookie
cookie = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/button')
cookie.click()

#accept cookie
singin = driver.find_element(By.XPATH,'/html/body/div[1]/header/div[1]/div/div[3]/div/button')
singin.click()
time.sleep(1)

#input username
emailbox = driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div/div/div/div/form[1]/div[2]/div/div[1]/input')
emailbox.send_keys(username)

#input password
passbox = driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div/div/div/div/form[1]/div[2]/div/div[2]/div/input')
passbox.send_keys(password)
time.sleep(1)

sin = driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div/div/div/div/form[1]/div[3]/div/button')
sin.click()
time.sleep(1)

actions = ActionChains(driver)
all = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[2]/div/div/div[1]/div[2]/a')
all.click()
time.sleep(1)

avaliable_con_col = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[3]/div/div/div[1]/div/div')
inner_html = avaliable_con_col.find_elements(By.CLASS_NAME,'event-item')
con = None
concert_found = False
for i ,each in enumerate(inner_html,start=1):
    title = each.find_element(By.CLASS_NAME,'title').text
    if title == data['target_con']:
        concert_found = True
        con = each
        break

if concert_found :
    con.find_element(By.CLASS_NAME,'btn-buynow').click()
    allrow = driver.find_elements(By.XPATH,'//*[@id="uMap2Map22"]/area')

    for zone in allrow:
        tar_zone = zone.get_attribute('href').split('#')
        if tar_zone[2] ==  data['target_zone']:
            zone.click()
    
    number = driver.find_element(By.XPATH,f'/html/body/div[2]/main/div/div[3]/div/div/div[1]/div/div[2]/form/ul/li/span[2]/select/option[{data["amount"]+1}]')
    number.click()

    confirm = driver.find_element(By.ID,'booknow')
    confirm.click()

    if data['get_ticket'] == 'self':
        pick = driver.find_element(By.ID,'btn_pickup')
    else:
        pick = driver.find_element(By.ID,'btn_thaipost')
    pick.click()

    mobile_pay = driver.find_element(By.ID,'btn_mobile')
    mobile_pay.click()

    truemoney = driver.find_element(By.ID,'btn_truemoney')
    truemoney.click()

    enter_number = driver.find_element(By.ID,'truemoney_contact')
    enter_number.send_keys(data['number'])
    
    checkbox = driver.find_element(By.ID,'checkagree')
    checkbox.click()
    
    # buy = driver.find_element(By.ID,'btn_mconfirm') 
    # buy.click()
    driver.execute_script("alert('กรุณากดปุ่มยืนยันเพื่อไปต่อ');")

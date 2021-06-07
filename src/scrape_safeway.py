import os
from selenium.webdriver.support import expected_conditions as EC
# from turtle import delay
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
# from PIL import Image
import io
# import requests
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException

# PROXY = "23.23.23.23:3128" # IP:PORT or HOST:PORT
# PROXY = "12.345.678.910:8080"

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)

# chrome = webdriver.Chrome(chrome_options=chrome_options)

# proxy_ip_port = "12.345.678.910:8080"
from selenium.webdriver.support.ui import WebDriverWait

proxy_ip_port = "173.254.206.34:3128"

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.sslProxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

DRIVER_PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH, desired_capabilities=capabilities)
driver.get('https://www.safeway.com/')
# driver.get('https://whatismyipaddress.com/')

time.sleep(5)
# element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'openFulfillmentModalButton')))
# driver.implicitly_wait(time_to_wait=)
driver.find_element_by_xpath('//*[@id="openFulfillmentModalButton"]').click()

time.sleep(1)

zip_field = driver.find_element_by_xpath(
    '//*[@id="storeFulfillmentModal"]/div/div/div[2]/store-fulfillment-tabs/div/div[1]/input')
zip_code = 94506
zip_field.send_keys(zip_code)
zip_field.send_keys(u'\ue007')

# driver.find_element_by_xpath('//*[@id="storeFulfillmentModal"]/div/div/div[2]/store-fulfillment-tabs/div/div[1]/span/svg').click()

time.sleep(2)

main_div = driver.find_element_by_xpath('//*[@id="fulfilmentInStore"]')

all_divs = main_div.find_elements_by_xpath('//div[@class="card-store row"]')

print(main_div)

for i in all_divs:
    if str(zip_code) in i.text:
        time.sleep(1)
        select = i.find_element_by_tag_name('a')
        if "Select" in select.text:
            select.click()
            print("pass")
        # i.find_element_by_xpath("//div[@class=btn btn-default card-store-btn btn-primary]").click()
        print(i.text)
        break

driver.quit()
# 94306
# //*[@id="storeFulfillmentModal"]/div/div/div[2]/store-fulfillment-tabs/div/div[1]/input
# driver.quit()

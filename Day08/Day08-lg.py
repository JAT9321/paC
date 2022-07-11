from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 抓拉钩

url = 'https://www.lagou.com/'
web = Edge()
web.get(url)
# 查找某个元素
el = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/p[1]/a')
el.click()
# 等待浏览器跳转
time.sleep(1)
# 获取输入框
el = web.find_element(By.XPATH, '//*[@id="search_input"]')
# 输入java 并按下enter
el.send_keys("java", Keys.ENTER)

# 获取列表内容
els = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div')

for el in els:
    name = el.find_element(By.XPATH, './div[1]/div[1]/div/a').text
    money = el.find_element(By.XPATH, './div[1]/div[1]/div[2]/span').text
    company = el.find_element(By.XPATH, './div[1]/div[2]/div[1]/a').text
    print(company, name, money)

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 跳转窗口
url = 'https://www.lagou.com/'

web = Edge()
web.get(url)

# 跳转到全国
web.find_element(By.XPATH, '//*[@id="changeCityBox"]/p[1]/a').click()
time.sleep(1)
# 输入java，并跳转
web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("java", Keys.ENTER)
time.sleep(0.5)
# 第一条信息，跳转
web.find_element(By.XPATH, '//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
time.sleep(1)
# 会出现新窗口，跳转到新窗口,-1代表最后出现的窗口
web.switch_to.window(web.window_handles[-1])
# 获取完整的职业描述
desc = web.find_element(By.XPATH, '//*[@id="job_detail"]/dd[2]/div').text
print(desc)
# 关闭当前窗口
web.close()
# 回到列表信息之前的窗口
web.switch_to.window(web.window_handles[0])
# 打印岗位名称信息
print(
    web.find_element(By.XPATH,
                     '/html/body/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[1]/a').text)

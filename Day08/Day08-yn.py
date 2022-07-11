from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.select import Select
import time

# 设置为不跳出浏览器界面
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')

# 艺恩年度票房
url = 'https://www.endata.com.cn/BoxOffice/BO/Year/index.html'

web = Edge(options=opt)
web.get(url)
# 定位到下拉框
select = web.find_element(By.XPATH, '//*[@id="OptionDate"]')
# 包装成下拉菜单，以便于下面进行遍历循环
select = Select(select)
# 选择下拉中的每个选项，
# 并取出对应年份的年度票房信息
for index in range(len(select.options)):
    # 通过索引获取
    select.select_by_index(index)
    # 通过下拉菜单中的每项option中的value取
    # select.select_by_value()
    time.sleep(2)
    # 得到整个票房table
    table = web.find_element(By.XPATH, '//*[@id="TableList"]/table')
    print(table.text)
    print("========================================================")
web.close()

import requests
from selenium import webdriver
import time
import datetime
import traceback

driver = "D:\\software\\program1\\edgedriver_win64\\msedgedriver.exe"
ID = '' #学号
pwd = '' #密码
sckey = '' # sever酱sckey


try:
    #edge驱动的位置
    driver = webdriver.Edge(driver)
    #在校学生临时出校申请（限当天出入）
    #//*[@id="printCasLogout"]
    driver.get("https://service.cau.edu.cn/v2/matter/detail?id=366")
    driver.implicitly_wait(5)
    time.sleep(5)
    print(driver.find_element_by_xpath('/html/body/div[1]/div[2]'))
    '''
    调用selenium库中的find_element_by_xpath()方法定位搜索框，
    同时使用send_keys()方法在其中输入信息
    '''
    #点击提交申请
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/button').click()
    #点击登录
    driver.find_element_by_xpath('//*[@id="un"]').send_keys(ID)
    driver.find_element_by_xpath('//*[@id="pd"]').send_keys(pwd)
    driver.find_element_by_xpath('//*[@id="index_login_btn"]/input').click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/button').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="pageBox"]/div[3]/div/table/tbody/tr[3]/td[2]/div/div[1]/div/input').send_keys('15030170131')

    driver.find_element_by_xpath('//*[@id="pageBox"]/div[3]/div/table/tbody/tr[4]/td[4]/div/div[1]/div/span/span/div[2]/input').send_keys("705")
    #目前体温 //*[@id="pageBox"]/div[3]/div/table/tbody/tr[5]/td[2]/div/div[1]/div/span/span/div[2]/input
    driver.find_element_by_xpath('//*[@id="pageBox"]/div[3]/div/table/tbody/tr[5]/td[2]/div/div[1]/div/span/span/div[2]/input').send_keys("36.1")
    # 外出去向
    driver.find_element_by_xpath('//*[@id="pageBox"]/div[4]/div/table/tbody/tr[3]/td[2]/div/div[1]/div/span/div[2]/textarea').send_keys("，")
    # 外出事由
    driver.find_element_by_xpath('//*[@id="pageBox"]/div[4]/div/table/tbody/tr[4]/td[2]/div/div[1]/div/span/div[2]/textarea').send_keys("，")
    #driver.find_element_by_xpath('//*[@id="pageBox"]/div[3]/div/table/tbody/tr[3]/td[2]').send_keys('15030170131')

    # 点击宿舍楼的下拉框
    driver.find_element_by_xpath('//*[@id="pageBox"]/div[3]/div/table/tbody/tr[4]/td[2]/div/div[1]/div/div/div/span/span/i').click()
    time.sleep(5)
    # 点击2号公寓南楼
    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[3]').click()

    # 点击 出入校区
    driver.find_element_by_xpath('//*[@id="pageBox"]/div[3]/div/table/tbody/tr[5]/td[4]/div/div[1]/div/div/div/span').click()
    time.sleep(5)
    # 点击 东校区
    driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[2]').click()

    # 预计外出时间
    driver.find_element_by_xpath('//*[@id="pageBox"]/div[4]/div/table/tbody/tr[1]/td[2]/div/div[1]/div/div/span[1]/i').click()
    time.sleep(5)
    today = str(datetime.date.today())
    #print(today)

    # 输入 外出日期 
    driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[1]/span[1]/div/input').send_keys(today)
    time.sleep(5)
    # 输入外出时间 /html/body/div[7]/div[1]/div/div[1]/span[2]/div[1]/input
    driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[1]/span[2]/div[1]/input').click()
    time.sleep(5)
    element = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[1]/span[2]/div[2]/div[1]/div/div[1]/div[1]/ul/li[7]')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(5)
    # 点击确定 
    driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[1]/span[2]/div[2]/div[2]/button[2]').click()
    
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/button[2]').click()
    time.sleep(5)
    # 预计返回时间 //*[@id="pageBox"]/div[4]/div/table/tbody/tr[1]/td[4]/div/div[1]/div/div/input
    driver.find_element_by_xpath('//*[@id="pageBox"]/div[4]/div/table/tbody/tr[1]/td[4]/div/div[1]/div/div/input').click()
    time.sleep(5)
    # 点击 21 /html/body/div[9]/div[1]/div/div[1]/div[1]/ul/li[18]
    element = driver.find_element_by_css_selector('body > div.el-time-panel.el-popper > div.el-time-panel__content > div > div:nth-child(1) > div.el-scrollbar__wrap > ul > li:nth-child(23)')
    driver.execute_script("arguments[0].click();", element)
    # 点击确定 /html/body/div[4]/div[2]/button[2]
    driver.find_element_by_css_selector('body > div.el-time-panel.el-popper > div.el-time-panel__footer > button.el-time-panel__btn.confirm').click()
    time.sleep(3)
    #点击正式提交
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div/button[2]').click()
    url = 'https://sctapi.ftqq.com/%s.send?text=申请出校成功啦~&desp=In carnage, I bloom like a flower in the dawn'%sckey
    requests.get(url)
except:
    print(traceback.format_exc()) 
    url = 'https://sctapi.ftqq.com/%s.send?text=申请出校失败咯……&desp=手动申请吧=='%sckey
    requests.get(url)



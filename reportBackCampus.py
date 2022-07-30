
# https://service.cau.edu.cn/v2/matter/todo

from logging import exception
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

    driver.get("https://service.cau.edu.cn/v2/matter/todo")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="un"]').send_keys(ID)
    driver.find_element_by_xpath('//*[@id="pd"]').send_keys(pwd)
    driver.find_element_by_xpath('//*[@id="index_login_btn"]/input').click()
    driver.implicitly_wait(5)
    ul = driver.find_element_by_xpath('//*[@id="todo"]/div[3]/section/div[1]/ul')
    lis = ul.find_elements_by_xpath('li')
    for i in range(len(lis)):
        lis[-1].click()
        driver.implicitly_wait(5)
        handles = driver.window_handles  # 获取当前浏览器所有窗口句柄
        driver.switch_to.window(handles[-1])
        driver.implicitly_wait(5)
        #点击 审批操作 - 提交
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/table/tr[1]/td[2]/label/span[2]').click()
        # 外出地点 /div[2]/button
        driver.find_element_by_xpath('//*[@id="pageBox"]/div[6]/div/table/tbody/tr[3]/td[1]/div/div[1]/div/span/span/div[2]/input').send_keys(',')
        # 停留时长
        driver.find_element_by_xpath('//*[@id="pageBox"]/div[6]/div/table/tbody/tr[3]/td[5]/div/div[1]/div/span/span/div[2]/input').send_keys("2h")
        # 乘坐交通工具
        
        driver.find_element_by_xpath('//*[@id="pageBox"]/div[6]/div/table/tbody/tr[3]/td[2]/div/div[1]/div/div/div/input').click()
        driver.implicitly_wait(3)
        driver.find_element_by_css_selector('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click() # 点击步行
        # 班次
        driver.find_element_by_xpath('//*[@id="pageBox"]/div[6]/div/table/tbody/tr[3]/td[3]/div/div[1]/div/span/span/div[2]/input').send_keys('1')
        #到达时间
        driver.find_element_by_xpath('//*[@id="pageBox"]/div[6]/div/table/tbody/tr[3]/td[4]/div/div[1]/div/div/input').click()
        today = str(datetime.date.today())
        driver.implicitly_wait(3)
        time.sleep(3)
        driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(1) > div > input').send_keys(today)#选择日期
        driver.implicitly_wait(3)
        time.sleep(3)
        driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(2) > div.el-input.el-input--small > input').click()#选择时间
        driver.implicitly_wait(3)
        time.sleep(3)
        driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(2) > div.el-time-panel.el-popper > div.el-time-panel__content > div > div:nth-child(1) > div.el-scrollbar__wrap > ul > li:nth-child(11)').click()##点击22
        driver.implicitly_wait(3)
        time.sleep(3)
        driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(2) > div.el-time-panel.el-popper > div.el-time-panel__footer > button.el-time-panel__btn.confirm').click()
        #确定
        driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-picker.el-popper.has-time > div.el-picker-panel__footer > button.el-button.el-picker-panel__link-btn.el-button--default.el-button--mini.is-plain').click()
        time.sleep(3)
        #实际外出时间
        driver.find_element_by_css_selector('#pageBox > div:nth-child(5) > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.dplugin-box.required.dplugin-box-1 > div > div').click()
        time.sleep(3)
        driver.find_element_by_css_selector('body > div:nth-child(12) > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(1) > div > input').send_keys(today)
        driver.implicitly_wait(3)
        time.sleep(3)
        """
        driver.find_element_by_css_selector('body > div:nth-child(12) > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(2) > div.el-input.el-input--small > input').click()
        driver.implicitly_wait(3)
        driver.find_element_by_css_selector('body > div:nth-child(12) > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(2) > div.el-time-panel.el-popper > div.el-time-panel__content > div > div:nth-child(1) > div.el-scrollbar__wrap > ul > li:nth-child(13)').click()
        driver.find_element_by_css_selector('body > div:nth-child(12) > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(2) > div.el-time-panel.el-popper > div.el-time-panel__footer > button.el-time-panel__btn.confirm').click()
        """
        driver.find_element_by_css_selector('body > div:nth-child(12) > div.el-picker-panel__footer > button.el-button.el-picker-panel__link-btn.el-button--default.el-button--mini.is-plain').click()
        driver.implicitly_wait(10)
        time.sleep(3)
        """ 
        element = driver.find_element_by_css_selector('body > div:nth-child(12) > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(1) > div > input')
        js = "arguments[0].value="+today+";"
        driver.execute_script(js, element)
        driver.implicitly_wait(10)
        time.sleep(3)
        """
        element = driver.find_element_by_css_selector('body > div:nth-child(12) > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(2) > div.el-input.el-input--small > input')
        driver.execute_script("arguments[0].click();", element)
        driver.implicitly_wait(10)
        time.sleep(3)
        element = driver.find_element_by_css_selector('body > div:nth-child(12) > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(2) > div.el-time-panel.el-popper > div.el-time-panel__content > div > div:nth-child(1) > div.el-scrollbar__wrap > ul > li:nth-child(2)')
        driver.execute_script("arguments[0].click();", element)
        driver.implicitly_wait(10)
        time.sleep(3)
        element = driver.find_element_by_css_selector('body > div:nth-child(12) > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(2) > div.el-time-panel.el-popper > div.el-time-panel__footer > button.el-time-panel__btn.confirm')
        driver.execute_script("arguments[0].click();", element)
        driver.implicitly_wait(10)
        time.sleep(3)
        driver.find_element_by_css_selector('body > div:nth-child(12) > div.el-picker-panel__footer > button.el-button.el-picker-panel__link-btn.el-button--default.el-button--mini.is-plain').click()
        #实际返回时间
        driver.find_element_by_css_selector('#pageBox > div:nth-child(5) > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > div > div.dplugin-box.required.dplugin-box-1 > div > div > input').click()
        driver.implicitly_wait(10)
        time.sleep(3)
        driver.find_element_by_css_selector('body > div:nth-child(13) > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(1) > div > input').send_keys(today)
        driver.implicitly_wait(10)
        time.sleep(3)
        driver.find_element_by_css_selector('body > div:nth-child(13) > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(2) > div.el-input.el-input--small').click()
        driver.implicitly_wait(10)
        time.sleep(3)
        element = driver.find_element_by_css_selector('body > div:nth-child(13) > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(2) > div.el-time-panel.el-popper > div.el-time-panel__content > div > div:nth-child(1) > div.el-scrollbar__wrap > ul > li:nth-child(24)')
        driver.execute_script("arguments[0].click();", element)
        driver.implicitly_wait(10)
        time.sleep(3)
        element = driver.find_element_by_css_selector('body > div:nth-child(13) > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(2) > div.el-time-panel.el-popper > div.el-time-panel__footer > button.el-time-panel__btn.confirm')
        driver.execute_script("arguments[0].click();", element)
        driver.implicitly_wait(10)
        time.sleep(3)
        driver.find_element_by_css_selector('body > div:nth-child(13) > div.el-picker-panel__footer > button.el-button.el-picker-panel__link-btn.el-button--default.el-button--mini.is-plain').click()
        js = "window.scrollBy(0,0);"
        driver.execute_script(js)
        driver.implicitly_wait(10)
        element = driver.find_element_by_css_selector('body > div.app.layout_two > div.content > div.examine_matter > div.operation_box > div.content > div.examine_action > div.submit_action > button')
        driver.execute_script("arguments[0].click();", element)
    url = 'https://sctapi.ftqq.com/%s.send?text=审批成功啦~&desp=In carnage, I bloom like a flower in the dawn'%sckey
    requests.get(url)
except:
    print(traceback.format_exc()) 
    url = 'https://sctapi.ftqq.com/%s.send?text=审批失败咯……&desp=手动审批吧=='%sckey
    requests.get(url)
    

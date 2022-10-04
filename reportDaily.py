import requests
from selenium import webdriver
import time
import traceback

"""
使用的edge浏览器，需要对应的驱动
上报成功sever酱会发送消息，需要有自己的sckey
"""
driver = "D:\\software\\program1\\edgedriver_win64\\msedgedriver.exe"
ID = '' #学号
pwd = '' #密码
sckey = '' # sever酱sckey
try:
    #edge驱动的位置
    driver = webdriver.Edge(driver)
    #cau疫情防控常态化管理系统 -- 每日上报
    driver.get("https://wep.cau.edu.cn/cauncovxs/wap/default/index")
    '''
    调用selenium库中的find_element_by_xpath()方法定位搜索框，
    同时使用send_keys()方法在其中输入信息
    '''
    #账号输入框
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/input').send_keys(ID)
    #密码输入框
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/input').send_keys(pwd)

    '''
    调用selenium库中的find_element_by_xpath()方法定位搜索按钮，
    同时使用click()方法对按钮进行点击
    '''
    #点击登录
    driver.find_element_by_xpath('//*[@id="app"]/div[3]').click()
    driver.implicitly_wait(5)
    time.sleep(5)
    #获取位置信息
    """
    js="document.getElementById('').scrollTop=100000" 
    driver.execute_script(js)
    """
    element = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[4]/ul/li[9]/div")
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(10)
    time.sleep(5)
    
    #7日内是否有共同居住者返京
    element = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[4]/ul/li[10]/div/div/div[2]")
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(10)
    time.sleep(5)
    
    #今日体温范围
    element = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[4]/ul/li[11]/div/div/div[2]")
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(10)
    time.sleep(5)
    
    #是否已接种疫苗
    element = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[4]/ul/li[12]/div/div/div[1]")
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(5)
    time.sleep(5)
    
    #疫苗接种地
    element = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[4]/ul/li[13]/div/div/div[1]")
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(5)
    time.sleep(5)
    #加强针
    element = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[4]/ul/li[14]/div/div/div[1]")
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(5)
    time.sleep(5)
    #今日同住人员
    element = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[4]/ul/li[25]/div/div/div[2]")
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(5)
    time.sleep(5)
    #昨日是否核酸，点“是“
    element = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[4]/ul/li[27]/div/div/div[1]")
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(5)
    time.sleep(5)
    
    #点击提交
    driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[5]/div").click()
    driver.implicitly_wait(5)
    time.sleep(5)
    #点击确认
    driver.find_element_by_xpath('//*[@id="wapcf"]/div/div[2]/div[2]').click()
    url = 'https://sctapi.ftqq.com/%s.send?text=上报成功啦~&desp=In carnage, I bloom like a flower in the dawn'%sckey
    requests.get(url)
except:
    print(traceback.format_exc()) 
    url = 'https://sctapi.ftqq.com/%s.send?text=上报失败咯……&desp=手动上报吧=='%sckey
    requests.get(url)
finally:
    driver.close()


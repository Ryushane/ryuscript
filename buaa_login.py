from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import signal

username_str = "xxx" # 你的校园网登陆用户名
password_str = "xxx" # 你的校园网登陆密码

can_connect = True

def login():
    try:
        driver = webdriver.Chrome()
        driver.get("https://gw.buaa.edu.cn") # 你的校园网登陆地址
        time.sleep(3)
        username_input = driver.find_element_by_id("username") # 校园网登陆用户名的输入控件ID, 浏览器上右键查看网页源代码查询
        password_input = driver.find_element_by_id("password") # 校园网登陆密码的输入控件ID, 浏览器上右键查看网页源代码查询
        print('Searching connect')
        login_button = driver.find_element_by_id("login") # 校园网登陆连接的点击控件ID, 浏览器上右键查看网页源代码查询
        print('Find connect successfully')
        username_input.send_keys(username_str)
        password_input.send_keys(password_str)
        print('Input user info')
        login_button.click()
        print('Connect')
        time.sleep(3)
    except:
        print("当前已经处于登录状态")
    finally:
        driver.close()

#主函数
def main():
    try:
        login()
    except:
        print("浏览器异常")

if __name__ == "__main__":
    main()
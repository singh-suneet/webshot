# made by R4J4
#Require selenium
#Require chromewebdriver
import random
from selenium import webdriver
import re
def banner():
    banner=""" 
               *******************************
               ************Web-Shot***********
               *******************************"""
    return banner


print(banner()+"\n"+"Welcome to Web-Shot, A simple Script to take screenshot of multiple IP addresses or domains. \n")

ip=list(re.split(',|\s', input("Enter either comma separated or space separated list of IPs or domains:\t"),))
print(ip)

def shot(ip):
 for i in ip:
    add = "https://" + i
    print(add)
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-logging')
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options) # add your chromedriver or geckodriver path
    driver.get("%s" %add)
    nam = i+'.png'
    driver.get_screenshot_as_file(nam)
    print("Screenshot taken \n")

shot(ip)
import sys
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

problem_url = input("problem url=https://leetcode.com/problems/fizz-buzz/description/") or 'https://leetcode.com/problems/fizz-buzz/description/' or sys.exit('Error: Problem url needed')
user = 'grekz'
pwd = getpass.getpass('Password:') or sys.exit('Pass needed')
browser = webdriver.Chrome("C:/git/helper-scripts/drivers/chromedriver.exe")
# browser = webdriver.Firefox()
browser.get('https://leetcode.com/accounts/login/')
elem = driver.find_element_by_id("id_login")
elem.send_keys(user)
elem = driver.find_element_by_id("id_password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
browser.get(problem_url)
# browser.close()
# TODO
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\Pichau\Desktop\bot_curtidas_instagram-master\geckodriver.exe')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/emailsignup/')
        time.sleep(2)
        email_elements = driver.find_element_by_xpath("//input[@name='emailOrPhone']")
        email_elements.clear()
        email_elements.send_keys(self.email)
        fullname_elements = driver.find_element_by_xpath("//input[@name='fullName']")
        fullname_elements.clear()
        fullname_elements.send_keys(self.fullname)
        username_elements = driver.find_element_by_xpath("//input[@name='username']")
        username_elements.clear()
        username_elements.send_keys(self.username)
        password_elements = driver.find_element_by_xpath("//input[@name='password']")
        password_elements.clear()
        password_elements.send_keys(self.password)
        password_elements.send_keys(Keys.RETURN)
        time.sleep(5)



botstarted = InstagramBot('oi','oiu','iu','oi')
botstarted.login()




#file_lines = emailgenerated.
#emailgenerated = open('emails_hisreadlines()
#last_line = [len(file_lines)-1]
#bot_wemail = InstagramBot(print(last_line))
#bot_wemail.login()


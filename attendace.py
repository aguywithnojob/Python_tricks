from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class attendance:
    def __init__(self,id,pas):
        self.id = id
        self.pas = pas
        self.bot = webdriver.Chrome(executable_path="E:\code\python\instabot\chromedriver_win32\chromedriver.exe")
    def login(self):
        bot = self.bot
        bot.get('http://housekeeping.tradeindia.com/')
        bot.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/form/div[1]/input').send_keys(self.id)
        bot.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/form/div[2]/input').send_keys(self.pas)
        bot.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/form/div[3]/input').send_keys(Keys.RETURN)
        
        try:
            other_login = bot.find_element_by_xpath('/html/body/div/div/div/div[4]/form/input[5]')
            if other_login:
                other_login.send_keys(Keys.RETURN)
        except Exception as e:
            pass

        bot.get('http://housekeeping.tradeindia.com/housekeeping/my_area/attendance_report.html')
        bot.get('http://housekeeping.tradeindia.com/housekeeping/my_area/attendance_report.html')
        bot.find_element_by_xpath('/html/body/div[2]/form/table/tbody/tr[2]/td/input').click()
        surplus = bot.find_element_by_xpath('/html/body/div[2]/table[3]/tbody').text
        return surplus

    def logout(self,report):
        bot = self.bot
        bot.find_element_by_xpath('/html/body/div[2]/div[6]/div[2]/a[2]').click()
        print(f'{report}')
        print('success attendance done...')
        bot.close()

if __name__ == '__main__':
    obj = attendance('Username','password')
    report = obj.login()
    time.sleep(8)
    obj.logout(report)
    
    
    
    

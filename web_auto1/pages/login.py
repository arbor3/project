from selenium import webdriver
from web_auto1.common.base import Base

url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"

class ZenTaoLogin(Base):

    def zentao_login(self, user='admin', pwd='123456'):
        user_loc = ('id', 'account')
        pwd_loc = ('name', 'password')
        login_loc = ('id', 'submit')

        self.send_keys(user_loc, user)
        self.send_keys(pwd_loc, pwd)
        self.click(login_loc)

    def is_login_success(self, _text):
        '''
        :param _text:
        :return:
        '''
        return self.is_title(_text)

    def is_login_fail(self):
        '''
        :param _text:
        :return:
        '''
        return self.is_alert()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    login = ZenTaoLogin(driver)
    login.login()
    title = "我的地盘 - 禅道"
    result = login.is_login_success(title)
    print(result)


import unittest
from web_auto1.pages.login import ZenTaoLogin
from selenium import webdriver

url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"

class TestLogin(unittest.TestCase):
# 1
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.login = ZenTaoLogin(self.driver)
        self.driver.get(url)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_01(self):
        '''正确的用户名和密码'''
        self.login.zentao_login()
        title = "我的地盘 - 禅道"
        rusult = self.login.is_login_success(title)
        self.assertTrue(rusult)

    def test_02(self):
        '''错误的用户名和密码'''
        self.login.zentao_login('admin1', '123456')
        rusult = self.login.is_login_fail()
        self.assertTrue(rusult)

if __name__ == '__main__':
    unittest.main()

# 111
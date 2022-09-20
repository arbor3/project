from pywinauto import Desktop
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException


class Base():

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20
        self.t = 0.5

   # TODO:共用方法

    def findElement(self, locator):
        '''等待模块'''
        # ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x:x.find_element(*locator))
        # return ele
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id", "value")')
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s" %(locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele

    def findElements(self, loctor):
        '''
        args
        locator 传元组
        '''
        try:
            eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*loctor))
            return eles
        except:
            return []

    def get_text(self, locator):
        return self.findElement(locator).text

    def send_keys(self, loctor, text):
        '''输入框模块'''
        ele = self.findElement(loctor)
        ele.send_keys(text)

    def click(self, loctor):
        '''点击按钮模块'''
        ele = self.findElement(loctor)
        ele.click()

    def clear(self, loctor):
        '''清空输入框模块'''
        ele = self.findElement(loctor)
        ele.clear()

    def isElementExsit(self, locator):
        '''查找约束的时候，存在返回element，不存在的时候Timeout异常'''
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def isElementExsit1(self, locator):
        els = self.findElements(locator)
        count = len(els) # 计算元素个数
        if count == 0:
            return False
        elif count == 1:
            return True
        else:
            print("定位到的元素个数：%s" %count)
            return True

    def is_title(self, _title):
        '''判断当前页面的title是否完全等于（==）预期字符串，返回布尔值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self, _title):
        '''判断当前页面的title是否包含预期字符串，返回布尔值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self, loctor, _text):
        '''判断某个元素中的text是否包含了预期的字符串，返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(loctor, _text))
            return result
        except:
            return False

    def is_value_in_element(self, loctor, _value):
        '''判断某个元素中的value属性是否包含了预期的字符串,value为空字符串，返回False'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(loctor, _value))
            return result
        except:
            return False

    def is_alert(self):
        '''判断是否是弹窗，'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def move_to_element(self, locator):
        '''鼠标事件'''
        ele = self.findElement(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def select_by_index(self, locator, index):
        '''通过索引，index是索引第几个，从0开始，默认选择第一个'''
        element = self.findElement(locator)
        Select(element).select_by_index(index)
        return element.click()

    def select_by_value(self, locator, value):
        '''通过value值定位'''
        element = self.findElement(locator)
        Select(element).select_by_value(value)
        return element.click()

    def select_by_text(self, locator, text):
        '''通过文本定位'''
        element = self.findElement(locator)
        Select(element).select_by_visible_text(text)
        return element.click()

    def js_scroll_end(self):
        '''滚动到底部'''
        js_heig = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.excute_script(js_heig)

    def js_focus(self, locator):
        '''聚焦元素---滚动到元素出现位置'''
        target = self.findElement(locator)
        js_heig = ""
        self.driver.excute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到底部'''
        js = "window.scrollTo(0, 0)"
        self.driver.excute_script(js)

if __name__ == '__main__':
    pass


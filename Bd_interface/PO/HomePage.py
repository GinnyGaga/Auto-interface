from utils.tools import find_element


class FindElement:
    def __init__(self, driver):
        self.id = ('id', 'kw')
        self.sb = ('id', 'su')
        self.driver = driver

    def get_element(self, key):
        # 1、输入关键字，并点击搜索
        find_element(self.driver, self.id).send_keys(key)
        find_element(self.driver, self.sb).submit()


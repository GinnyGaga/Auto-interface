# -*- coding: utf-8 -*-

from cases.common import get_all
from common import CommonPage


class OP(CommonPage):
    def test01(self):
        print("01 获取百度首页的返回值")
        current_url = self.driver.current_url
        return get_all(current_url)

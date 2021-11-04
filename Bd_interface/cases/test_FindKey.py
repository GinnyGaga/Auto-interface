from cases.common import CommonPage
from PO.HomePage import FindElement
from cases.common import get_all


class OP(CommonPage):
    def test01(self):
        print("02 获取查询关键字的返回值")
        FindElement(self.driver).get_element("淘宝")
        current_url = self.driver.current_url
        return get_all(current_url)



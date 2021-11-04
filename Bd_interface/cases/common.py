# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import unittest
import requests
import json
import warnings


class CommonPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        chromedriver = "D:\\Work\\PycharmProjects\\Bd_interface\\chromedriver\\chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.get("https://www.baidu.com/")
        cls.driver.maximize_window()
        print("打开百度首页")
        driver = cls.driver

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        cls.driver.quit()
        print("关闭百度首页")

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        pass


def get_all(get_url):

    sess = requests.session()  # 获取当前请求的会话
    req = sess.get(url=get_url)  # 传入URL，获取当前URL请求值
    # 将请求头的User-Agent替换为浏览器，否则会获取不到完整的响应内容（浏览器防爬虫）
    req.request.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    print(req.request.headers)
    try:
        res = requests.get(url=get_url)  # 获取返回值
        print("响应状态码为：%s" % res.status_code)  # 获取返回状态码
        # res_headers = json.dumps(dict(res.headers), indent=2, sort_keys=True)  # 将字典格式的响应头转换为JSON字符串
        # print("响应头为：\n %s " % res_headers)
        # print("响应cookies为：\n %s " % res.cookies)
        # print("响应内容为：\n %s " % res.text)
        print("响应内容为：\n %s " % res.content)
    except Exception as e:
        print(e)






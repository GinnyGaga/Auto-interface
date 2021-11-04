import unittest
from utils.HTMLTestRunner import HTMLTestRunner

testcases = unittest.defaultTestLoader.discover('cases','test_*.py')
testSuite = unittest.TestSuite()
testSuite.addTests(testcases)

title = '测试报告'
desc = '环境：windows 10 浏览器：chrome'
report = './report/report.html'

with open(report, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title=title, description=desc, tester='Ginny')
    runner.run(testSuite)

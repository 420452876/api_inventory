import unittest,HTMLTestRunner_PY3

from TestCase.customer_params import TestCustomer
from TestCase.stock_params import TestStock
from app import BASE_DIR
from TestCase.category_params import TestCate

suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestCate))
suite.addTest(unittest.makeSuite(TestStock))
suite.addTest(unittest.makeSuite(TestCustomer))

filename = BASE_DIR + "/report/test.html"

with open(filename, mode='wb') as f :
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=2,title='进销存管理系统报告',description="进销存管理系统测试报告生成")
    runner.run(suite)
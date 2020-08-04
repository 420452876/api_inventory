import unittest,app,logging

from api.category_api import Category_api
from api.stock_api import Stock_api
from tools.read_stock import assert_stock,get_stock
from parameterized import parameterized

class TestStock(unittest.TestCase):
    def setUp(self):
        self.cate_api = Category_api()
        self.stock_api = Stock_api()

    # 新增库存
    @parameterized.expand(get_stock('add_stock'))
    def test01_stock_add(self,http_code,provider,model,price,inventory,quantity):
        # 添加分类
        response = self.cate_api.cate_add()
        logging.info("添加分类结果为：{}".format(response.json()))
        # 获取分类id
        app.CATE_ID = response.json().get('Id')
        logging.info("当前分类id为：{}".format(app.CATE_ID))

        # 添加品牌
        response = self.cate_api.brand_add(app.CATE_ID)
        logging.info("添加品牌结果为：{}".format(response.json()))
        # 获取品牌id
        app.B_ID= response.json().get('Id')
        logging.info("当前分类id为：{}".format(app.CATE_ID))
        # 调用封装好得接口
        response = self.stock_api.stock_add()
        logging.info("添加的库存结果为：{}".format(response.json()))
        app.STO_ID = response.json().get('Id')

        # 调用工具类断言接口
        assert_stock(self,response,http_code,provider,model,price,inventory,quantity)


    # 查询新添加的库存
    def test02_stock_select(self):
        response = self.stock_api.stock_select()
        jsonData = response.json()
        for data in jsonData :

            if data.get('Id') == app.STO_ID:
                # 断言新添加的库存id
                self.assertEqual(app.STO_ID,data.get('Id'))

        # 断言状态
        self.assertEqual(200,response.status_code)

    # 修改库存
    @parameterized.expand(get_stock('upd_stock'))
    def test03_stock_upd(self,http_code,provider,model,price,inventory,quantity):

        response = self.stock_api.stock_upd(app.STO_ID)
        logging.info('修改库存结果为：{}'.format(response.json()))

        # 断言状态
        assert_stock(self,response,http_code,provider,model,price,inventory,quantity)

    # 出库
    @unittest.skip('跳过该用例')
    def test_03_stock_out(self):
        response = self.stock_api.stock_out(app.STO_ID)
        logging.info("出库结果为：{}".format(response.json()))

    # 删除库存
    def test04_stock_del(self):
        response = self.stock_api.stock_del(app.STO_ID)

        # 断言状态
        self.assertEqual(200,response.status_code)
import unittest,logging,app

from parameterized import parameterized

from api.customer_api import Customer_api
from tools.read_customer import assert_cutomer,get_cust


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.cust_api = Customer_api()

    # 新增顾客
    @parameterized.expand(get_cust('add_cust'))
    def test01_cust_add(self,http_code,shipper,model,name,phone,address):

        response = self.cust_api.customer_add()
        logging.info("添加的顾客结果为：{}".format(response.json()))

        # 获取顾客id
        app.CUST_ID = response.json().get('Id')
        logging.info("获取的顾客id为：{}".format(app.CUST_ID))
        # 调用工具类断言接口
        assert_cutomer(self,response,http_code,shipper,model,name,phone,address)


    # 修改顾客
    @parameterized.expand(get_cust('upd_cust'))
    def test02_cust_upd(self,http_code,shipper,model,name,phone,address):

        response = self.cust_api.customer_upd(app.CUST_ID)
        # 调用工具类断言接口
        assert_cutomer(self, response, http_code, shipper, model, name, phone, address)


    # 查询新增的顾客
    def test03_cust_select(self):
        response = self.cust_api.customer_select()
        jsonData = response.json()

        for data in jsonData :
            data.get('Id')
            if data.get('Id') == app.CUST_ID:
                # 断言新增的顾客id
                self.assertEqual(app.CUST_ID,data.get('Id'))

        # 断言状态
        self.assertEqual(200,response.status_code)

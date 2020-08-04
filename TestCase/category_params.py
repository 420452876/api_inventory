import unittest,logging,app,requests


from api.category_api import Category_api

class TestCate(unittest.TestCase):
    def setUp(self):
        self.cate_api = Category_api()

    # 添加分类
    def test01_cate_add(self):
        response = self.cate_api.cate_add()
        logging.info("添加的分类结果为：{}".format(response.json()))

        # 获取分类的id保存在全局变量中
        app.CATE_ID = response.json().get('Id')
        logging.info("添加的分类id为：{}".format(app.CATE_ID))

        # 断言状态
        self.assertTrue(200,response.status_code)
        # 断言分类名称
        self.assertEqual("电脑",response.json().get('Name'))

    def test02_cate_select(self):
        response = requests.get("http://localhost/category")
        logging.info("查询结果为：{}".format(response.json()))
        jsonData = response.json()
        for i in jsonData :
            cid = i.get('Id')
            if cid == app.CATE_ID :
                self.assertTrue(cid,app.CATE_ID)

    # 添加品牌
    def test03_brand_add(self):
        response = self.cate_api.brand_add(app.CATE_ID)
        logging.info("添加的品牌结果为：{}".format(response.json()))

        # 获取品牌的id，保存在全局变量中
        app.B_ID = response.json().get('Id')
        logging.info("添加的品牌id为：{}".format(app.B_ID))
        # 断言状态
        self.assertTrue(200, response.status_code)
        # 断言品牌名称
        self.assertEqual("联想电脑",response.json().get('Name'))

    # 删除品牌
    def test04_brand_del(self):
        response = self.cate_api.cate_del(app.B_ID)
        # 断言状态
        self.assertTrue(200,response.status_code)

    # 删除分类
    def test05_cate_del(self):
        response = self.cate_api.cate_del(app.CATE_ID)
        # 断言状态
        self.assertTrue(200, response.status_code)
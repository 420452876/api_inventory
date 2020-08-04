from app import BASE_DIR
import json

# 定义工具类 封装通用断言函数
def assert_stock(self,response,http_code,Provider,Model,Price,Quantity,Inventory):
    # 断言响应状态
    self.assertEqual(http_code, response.status_code)
    # 断言响应体
    self.assertEqual(Provider, response.json().get('Provider'))
    self.assertEqual(Model, response.json().get('Model'))
    self.assertEqual(Price, response.json().get('Price'))
    self.assertEqual(Quantity, response.json().get('Quantity'))
    self.assertEqual(Inventory, response.json().get('Inventory'))


# 获取修改库存json参数
# case = add_stock 或 upd_stock
def get_stock(case):
    filename = BASE_DIR + "/data/stock_data.json"
    with open(filename,'r',encoding='utf-8') as f :
        jsonData = json.load(f)

        if jsonData.get(case) :
            data = jsonData.get(case)

            case_list = []
            http_code = data.get('http_code')
            provider = data.get('Provider')
            model = data.get('Model')
            price = data.get('Price')
            inventory = data.get('Inventory')
            quantity = data.get('Quantity')
            case_list.append((http_code,provider,model,price,inventory,quantity))
            return case_list



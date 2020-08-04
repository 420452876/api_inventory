import json
from app import BASE_DIR
# 定义工具类,封装通用的断言函数
def assert_cutomer(self,response,http_code,Shipper,Model,Name,Phone,Address):
    # 断言请求响应
    self.assertEqual(http_code,response.status_code)
    # 断言响应体
    self.assertEqual(Shipper, response.json().get('Shipper'))
    self.assertEqual(Model, response.json().get('Model'))
    self.assertEqual(Phone, response.json().get('Phone'))
    self.assertEqual(Address, response.json().get('Address'))
    self.assertEqual(Name, response.json().get('Name'))

# 获取添加顾客json参数

def get_cust(case):
    filename = BASE_DIR + "/data/cust_data.json"
    with open(filename,'r',encoding='utf-8') as f :
        jsonData = json.load(f)
        data = jsonData.get(case)
        case_list = []
        http_code = data.get("http_code")
        shipper = data.get('Shipper')
        model = data.get('Model')
        name = data.get('Name')
        phone = data.get('Phone')
        address = data.get('Address')

        case_list.append((http_code,shipper,model,name,phone,address))
        return case_list





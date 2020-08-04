# 封装 顾客 api
import datetime
import requests,time

class Customer_api :

    # 添加顾客 api
    def customer_add(self):
        # 获取明天的时间戳
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        nexttime = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d')) * 1000)

        url_add = "http://localhost/customer"

        data = {
            "Shipper": "蔡文姬",
            "Model": "vivo",
            "Name": "小赵",
            "Phone": "13511112222",
            "Address": "深圳",
            "SaleDate": int(time.time() * 1000),
            "DeliveryDate": nexttime,
            "Status": 1
        }
        return requests.post(url_add, data=data)

    # 修改顾客 api
    def customer_upd(self,custid):
        url_upd = "http://localhost/customer/" + custid
        data = {
            "Shipper": "潇洒",
            "Model": "oppo",
            "Name": "加油",
            "Phone": "13455556666",
            "Address": "深圳南山",
            "SaleDate": int(time.time() * 1000),
            "DeliveryDate": int(time.time() * 1000),
            "Status": 1
        }

        return requests.put(url_upd,data=data)

    # 查询顾客 api
    def customer_select(self):
        url_select = "http://localhost/customer"
        return requests.get(url_select)
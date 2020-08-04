# 封装 库存 api
import requests,app,time

class Stock_api:
    # 封装 添加库存
    def stock_add(self):
        add_url = "http://localhost/stock"
        data = {
            "Provider":"超云",
            "Bid":app.B_ID,
            "Model":"鼠标",
            "Date": int(time.time()*1000),
            "Price":110,
            "Inventory":10,
            "Quantity":10
        }

        return requests.post(add_url,data=data)

    # 封装 查询新添加的库存
    def stock_select(self):
        select_url = "http://localhost/stock"
        return requests.get(select_url)

    # 封装 更改库存
    def stock_upd(self,stoid):
        upd_url = "http://localhost/stock/" + stoid
        data = {
            "Provider": "狗蛋",
            "Model": "显示器",
            "Price":200,
            "Inventory": 20,
            "Quantity": 20
        }

        return requests.put(upd_url,data)

    # 封装 删除库存
    def stock_del(self,stoid):
        del_url = "http://localhost/stock/" + stoid
        return requests.delete(del_url)

    # 封装 出库
    def stock_out(self,stoid):
        out_url = "http://localhost/saled"
        data = {
            "Shipper":"阿超",
            "Date":int(time.time()*1000),
            "Quantity":1,
            "Price":500,
            "Sid":stoid
        }
        return requests.post(out_url,data=data)
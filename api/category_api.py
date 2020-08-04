# 封装 品类 api
import  requests

class Category_api :
    # 封装添加分类接口
    def cate_add(self):
        add_url = "http://localhost/category"
        data = {'name':'电脑'}
        return requests.post(add_url,data=data)

    # 封装添加品牌接口
    def brand_add(self,cate_id):
        add_brand_url = "http://localhost/category"
        data = {'name':'联想电脑','pid':cate_id}
        return requests.post(add_brand_url,data=data)

    # 封装删除品牌接口
    def brand_del(self,b_id):
        del_brand_url = "http://localhost/category/" + b_id
        return requests.delete(del_brand_url)

    # 封装删除分类接口
    def cate_del(self,cate_id):
        del_cate_url = "http://localhost/category/" + cate_id
        return requests.delete(del_cate_url)
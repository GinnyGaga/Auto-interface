from config import host
import requests


class Api:
    # 1、初始化
    def __init__(self,case):
        # 1、提取 url = host+path
        self.url = host + case.get("path")
        # 2、请求方法
        self.method = case.get("method")
        # 3、请求参数类型
        self.param_type = case.get("param_type")
        # 4、请求信息头
        self.headers = case.get("headers")
        # 5、请求参数
        self.params = case.get("params")

    # 2、查询方法
    def _get(self):
        return requests.get(url=self.url,params=self.params,headers=self.headers)

    # 3、新增方法
    def _post(self):
        # 判断参数类型是json还是data
        if self.param_type == "json":
            return requests.post(url=self.url, json=self.params, headers=self.headers)
        elif self.param_type == "data":
            return requests.post(url=self.url, data=self.params, headers=self.headers)

    # 4、更新方法
    def _put(self):
        return requests.put(url=self.url,json=self.params,headers=self.headers)

    # 5、删除方法
    def _delete(self):
        return requests.delete(url=self.url,params=self.params,headers=self.headers)

    # 6、调用运行方法
    def run_method(self):
        if self.method == "get":
            return self._get()
        elif self.method == "post":
            return self._post()
        elif self.method == "put":
            return self._post()
        elif self.method == "delete":
            return self._delete()



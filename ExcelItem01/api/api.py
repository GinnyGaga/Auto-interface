from config import host


class Api:
    # 1、初始化
    def __init__(self,case):
        # 1、提取 url = host+path
        self.url = host + case.get("path")
        # 2、请求方法
        self.method = case.get("method")
        # 3、请求参数类型
        self.param_type = case.get("method")
        # 4、请求信息头
        self.headers = case.get("headers")
        # 5、请求参数
        self.params = case.get("params")

        pass

    # 2、查询方法
    def _get(self):
        pass

    # 3、新增方法
    def _post(self):
        pass

    # 4、更新方法
    def _put(self):
        pass

    # 5、删除方法
    def _delete(self):
        pass

# 6、调用运行方法


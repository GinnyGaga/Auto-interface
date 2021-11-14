from tools.get_log import GetLog

log = GetLog.get_logger()


def common_assert(response, case):
    log.info("正在调用断言公共方法")
    # 获取响应数据
    result = response.json()
    # 获取预期数据
    expect = case["expect"]
    # # 断言 响应状态吗
    # assert response.status_code == expect.get("code"), \
    #     "错误！响应 code：{} 预期code：{}".format(response.status_code, expect.get("code"))
    # 断言 status
    assert result["status"] == expect["status"], \
        "错误！响应 status：{} 预期 status：{}".format(result["status"], expect["status"])
    # 断言 data
    assert result["data"] == expect["data"], \
        "错误！响应 data：{} 预期 data：{}".format(
        result["data"], expect["data"])

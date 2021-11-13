from tools.get_log import GetLog

log = GetLog.get_logger()


def common_assert(response, case):
    log.info("正在调用断言公共方法")
    # 获取响应数据
    result = response.json()
    # 获取预期结果
    expect = case.get("expect")
    # 断言 响应状态码,自定义异常信息
    assert response.status_code == expect.get("code"), \
        "错误！响应状态码：{}，预期状态码：{}".format(response.status_code, expect.get("code"))
    # 断言 success
    assert result.get("success") == expect.get("result").get("success"), \
        "错误！响应success：{}，预期success：{}".format(result.get("success"), expect.get("result").get("success"))
    # 断言 code
    assert result.get("code") == expect.get("result").get("code"), \
        "错误！响应code：{}，预期code：{}".format(result.get("code"), expect.get("result").get("code"))
    # 断言 message
    assert result.get("message") == expect.get("result").get("message"), \
        "错误！响应code：{}，预期code：{}".format(result.get("message"), expect.get("result").get("message"))

from Api.apiFactory import ApiFactory
import app, utils, pytest,logging


@pytest.mark.run(order=0)
class TestUserApi:

    def test_get_token(self):
        """获取token"""
        # 响应对象
        res = ApiFactory.get_user_api().get_token_api()
        # 打印 请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言token存在
        assert len(res.json().get("token")) > 0
        # 保存token 到 app配置文件
        app.headers["token"] = res.json().get("token")
        print("app.headers:{}".format(app.headers))

    def test_verify_token(self):
        """验证token"""

        # 响应对象
        res = ApiFactory.get_user_api().verify_token_api()
        # 打印 请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言有效
        assert res.json().get("isValid") is True

    def test_user_address(self):
        """用户地址信息"""
        # 响应对象
        res = ApiFactory.get_user_api().user_address_api()
        # 打印 请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言信息
        assert False not in [i in res.text for i in ["大王", "13888888888", "上海市", "普能东新区", "111号"]]

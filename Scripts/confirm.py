from Api.apiFactory import ApiFactory

# # 调用轮播图api
# print("轮播图:{}".format(ApiFactory.get_home_api().banner_api().json()))
#
# # 调用主题
# print("主题:{}".format(ApiFactory.get_home_api().theme_api().json()))
#
# # 调用最新新品
# print("最近新品:{}".format(ApiFactory.get_home_api().recent_product_api().json()))

# # 调用 商品分类
# print("分类:{}".format(ApiFactory.get_product_api().product_classify_api().json()))
#
# # 调用分类下商品
# print("分类下商品:{}".format(ApiFactory.get_product_api().classify_product_api(5).json()))
# # 调用商品信息
# print("商品信息:{}".format(ApiFactory.get_product_api().product_detail_api(26).json()))

# 调用用户获取token

# print("生成token:{}".format(ApiFactory.get_user_api().get_token_api().json()))

"""需要在app.py的headers中添加token才可以验证 否则需要运行测试脚本才可以对headers赋值"""
print("查看订单:{}".format(ApiFactory.get_order_api().order_list_api().json()))

print("创建订单:{}".format(ApiFactory.get_order_api().create_order_api(12, 7).json()))

print("查看订单:{}".format(ApiFactory.get_order_api().query_order_api(120).json()))

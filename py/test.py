a = "goods_name=reru647324ewk&mch_id=100001001&mch_order_no=2387fhsgfjsdfsjdkf&mch_return_msg=test=1&notify_url=http://google.com&order_date=2022-10-11 20:33:41&page_url=http://google.com&pay_type=101&trade_amount=100&version=1.0&key=D76276295D6F43C49D9E450327AF4D2F";
for text in a.split("&"):
    print('map.put("%s","%s");' % (text.split("=")[0],text.split("=")[1]))

#coding=utf-8
import jpush

callback_url = ''
app_key = 'cd4f398315d09bxxxxxxxxxx'
app_secret = 'ad59ef62403130xxxxxxxxxx'

imei = '353918059xxxxxx'

#唯一编号
sendno = 222
desc = '测试薇密jpush推送'
title = '薇密安卓测试'
content = '薇密安卓推送测试 python api'

jp = jpush.JpushClient(app_key, app_secret, callback_url)
jp.send_notification_with_imei(imei, app_key, sendno, desc, title, content, 'android')

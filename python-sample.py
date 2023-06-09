import os
import numpy as np
import glob

a = np.array([1, 2])
b = np.array([3, 4])
print(a + b)

import datetime
dt_now = datetime.datetime.now()
print(dt_now)

dt_now_jst_aware = datetime.datetime.now(
    datetime.timezone(datetime.timedelta(hours=9))
)
print(dt_now_jst_aware)
print(dt_now_jst_aware.tzinfo)
print(dt_now_jst_aware.strftime("%Y%m%d%H%M"))

dt = dt_now_jst_aware.strftime("%Y%m%d%H")
# dt = "2022042523"
print("dt : " + dt)
files = './tweets/' + dt + '_*.tw'
plist = glob.glob(files)
if len(plist) < 1:
	exit()
file = plist[0]


isExists = os.path.exists(file) 
print(isExists)
if isExists != True:
	exit()

f = open(file, 'r', encoding='UTF-8')
data = f.read()
print(data)
f.close()

#exit()


# ツイートを取得
import tweepy
import time
import glob

# 取得した各種キーを格納---------------------------------------------
consumer_key ="j1jnmxi0dVK8WxsiVksWrValm"
consumer_secret ="MATCPIUyxXtrQQviDHfMVEzQxGYqU3LGiZ1GXWWjRYWKvDrS19"
access_token="3009736928-GlNRGtJXSQ3kPlhBUnGjkfLTdwhTcpY4yIbQKGC"
access_token_secret ="qxgUKAMcaqQ4F0bYtfuNSmDkN4vdaKfde2dNtoUpqWFhl"

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#-------------------------------------------------------------------

#ツイートを投稿
#api.update_status("シグナル通り翌日急落。。。")

#画像付きツイート
#api.update_with_media(status = '本日のチャート\n9101', filename = '/var/www/tmp/charts/20211210/9101.png')

#from gs import gsp
#data = gsp.getTweetList()
#print(data)
if data is not None:
    api.update_status(data)



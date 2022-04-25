import numpy as np

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
file = './tweets/schedule-tweet-' + dt + '.tw'
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
consumer_key ="6X5WoqpjShCgPVvipQQ6aEVLm"
consumer_secret ="FdRkKXpdcM3WUD3cNHet1FeBSEJbqt40bQTe2uYvUqQAqDtsau"
access_token="3009736928-IvceHOtALGPI3b0Od2kWE7r1OKxP8fbVpIwsfIP"
access_token_secret ="WYhXGZ07p0ZNqH6LMNfSD19OQob08DSul1lsSrIwvly2U"

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



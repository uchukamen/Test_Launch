# mp4 を twitter にポストする
#
import tweepy
import datetime

# 認証に必要なキーとトークン
API_KEY = '0YGqpHd02U5lC25TLTFxEQ3ag'
API_SECRET = 'OQ5tlqCJyeTSqwWXdg75pzCFKnqfgyT6B8BLMkcP0pRNyDNQzh'
ACCESS_TOKEN = '1326821144905707522-MIhnMGkFyJl9GUa6QVXgLA3Rq1LNT5'
ACCESS_TOKEN_SECRET = 'LlUO6EPDcr91eTeVpe30EqsdMqrtytOJrHz2pcOGFRFLS'

# APIの認証
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# キーワードからツイートを取得
api = tweepy.API(auth)

t = datetime.datetime.now()

# メッセージ
m1 = "島根県美郷町 野間雲海ビュースポット ライブカメラ \n"
m2 = datetime.datetime.strftime(t, "\t%Y/%m/%d %H:%M\n")
m3 = "https://www.youtube.com/watch?v=T_Qe2P2GvUs\n"
m4 = "より、今朝のタイムラプス自動生成テスト中\n"
m5 = "\n"
m6 = "雲海検出の説明: https://aiharasoft.com/wordpress/misato/\n"
m7 = "\n"
m8 = "美郷町雲海予報: https://gov.town.shimane-misato.lg.jp/unkai/\n"
m9 = "\n"
m10 = "#雲海 #美郷町 #美郷町雲海 #美郷町雲海検出"
message = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9 + m10

# 静止画
# filename = "20211022074100.jpg"

# 動画
dir = "/Users/uchukamen/Documents/Unkai_Misato/video/"
filename = datetime.datetime.strftime(t, "%Y%m%d.mp4")
videopath = dir + filename
print(videopath)

upload_result = api.media_upload(videopath)
api.update_status(status=message, media_ids=[upload_result.media_id_string])
# api.update_status(status=message)

print("tweet 完了")
